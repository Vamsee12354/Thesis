from __future__ import annotations

import csv
import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

TASK_NUMBER = 8
PILOT_MODE = False
OVERWRITE_PREVIOUS_RESULTS = True
TIMEOUT_SECONDS = 60

BASE_DIR = Path(r"C:\Users\kalup\Desktop\Thesis")
MODELS = ["deepseek", "gemma", "mistral", "openai", "amazon"]
ALL_SOURCES = MODELS + ["manual"]
RUNS = range(1, 11)

MANUAL_TASK_FOLDERS = {
    1: "task1_unique_brands",
    2: "task2_get_average_price",
    3: "task3_get_min_attribute",
    4: "task4_get_reading_duration",
    5: "task5_validate_contact_form",
    6: "task6_validate_password",
    7: "task7_product_list_live_v",
    8: "task8_slugify",
    9: "task9_product_cache_get",
}

OUTPUT_DIR = BASE_DIR / "automation_output"
WORK_DIR = OUTPUT_DIR / "_temporary_execution"
LOG_DIR = OUTPUT_DIR / "execution_logs"
MATRIX_CSV = OUTPUT_DIR / f"task_{TASK_NUMBER}_execution_matrix.csv"
FAILED_TESTS_CSV = OUTPUT_DIR / f"task_{TASK_NUMBER}_failed_tests.csv"
REVIEW_CSV = OUTPUT_DIR / f"task_{TASK_NUMBER}_review_sheet.csv"

MATRIX_HEADERS = ["task", "run", "test_source", "implementation_source", "test_file", "implementation_file", "passed_tests", "failed_tests", "error_tests", "skipped_tests", "total_tests", "complete", "return_code", "log_file", "investigation_status", "failure_cause", "error_category", "manual_notes"]
FAILED_TEST_HEADERS = ["task", "run", "test_source", "implementation_source", "test_name", "result_type", "log_file", "failure_cause", "error_category", "manual_notes"]
REVIEW_HEADERS = ["Run", "Test LLM", "Implementation LLM", "Passed tests", "Total Tests", "Complete?", "Notes"]


def get_test_file(task: int, run: int, test_source: str) -> Path:
    if test_source == "manual":
        return BASE_DIR / "src" / MANUAL_TASK_FOLDERS[task] / "tests.py"
    return BASE_DIR / "generated_tests" / test_source / f"task_{task}" / f"run_{run:02d}_test.py"


def get_implementation_file(task: int, run: int, implementation_source: str) -> Path:
    if implementation_source == "manual":
        return BASE_DIR / "src" / MANUAL_TASK_FOLDERS[task] / "implementation_manual.py"
    return BASE_DIR / "results" / implementation_source / f"task_{task}" / f"run_{run:02d}.py"


def create_csv_if_missing(path: Path, headers: list[str]) -> None:
    if not path.exists():
        with path.open("w", newline="", encoding="utf-8") as csv_file:
            csv.DictWriter(csv_file, fieldnames=headers).writeheader()


def append_csv_row(path: Path, headers: list[str], row: dict) -> None:
    with path.open("a", newline="", encoding="utf-8") as csv_file:
        csv.DictWriter(csv_file, fieldnames=headers).writerow(row)


def load_completed_combinations() -> set[tuple[str, str, str]]:
    completed = set()
    if OVERWRITE_PREVIOUS_RESULTS or not MATRIX_CSV.exists():
        return completed
    with MATRIX_CSV.open("r", newline="", encoding="utf-8") as csv_file:
        for row in csv.DictReader(csv_file):
            completed.add((row["run"], row["test_source"], row["implementation_source"]))
    return completed


def create_review_sheet() -> None:
    if not MATRIX_CSV.exists():
        return
    display_names = {"deepseek": "Deepseek", "gemma": "Gemma", "mistral": "Mistral", "openai": "OpenAI", "amazon": "Amazon", "manual": "Manual"}
    with MATRIX_CSV.open("r", newline="", encoding="utf-8") as csv_file:
        matrix_rows = list(csv.DictReader(csv_file))
    blank = {header: "" for header in REVIEW_HEADERS}
    with REVIEW_CSV.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=REVIEW_HEADERS)
        writer.writeheader()
        for run in sorted({int(row["run"]) for row in matrix_rows if row["run"]}):
            run_rows = [row for row in matrix_rows if row["run"] == str(run)]
            for test_source in ALL_SOURCES:
                suite_rows = [row for row in run_rows if row["test_source"] == test_source]
                suite_rows.sort(key=lambda row: ALL_SOURCES.index(row["implementation_source"]))
                for row in suite_rows:
                    writer.writerow({
                        "Run": row["run"],
                        "Test LLM": display_names[row["test_source"]],
                        "Implementation LLM": display_names[row["implementation_source"]],
                        "Passed tests": row["passed_tests"],
                        "Total Tests": row["total_tests"],
                        "Complete?": row["complete"],
                        "Notes": "" if row["complete"] == "Yes" else "To investigate",
                    })
                writer.writerow(blank)
            writer.writerow(blank)


def parse_unittest_output(output: str) -> dict:
    total_match = re.search(r"Ran\s+(\d+)\s+test(?:s)?", output, flags=re.IGNORECASE)
    failures_match = re.search(r"failures=(\d+)", output, flags=re.IGNORECASE)
    errors_match = re.search(r"errors=(\d+)", output, flags=re.IGNORECASE)
    skipped_match = re.search(r"skipped=(\d+)", output, flags=re.IGNORECASE)
    total = int(total_match.group(1)) if total_match else 0
    failures = int(failures_match.group(1)) if failures_match else 0
    errors = int(errors_match.group(1)) if errors_match else 0
    skipped = int(skipped_match.group(1)) if skipped_match else 0
    return {"passed": max(total - failures - errors - skipped, 0), "failed": failures, "errors": errors, "skipped": skipped, "total": total}


def get_failed_test_events(output: str) -> list[tuple[str, str]]:
    events = []
    pattern = r"^(.+?)\s+\((.+?)\)\s+\.\.\.\s+(FAIL|ERROR|UNEXPECTED SUCCESS)$"
    for line in output.splitlines():
        match = re.match(pattern, line.strip())
        if match:
            events.append((f"{match.group(1)} ({match.group(2)})", match.group(3).lower().replace(" ", "_")))
    if not events and any(text in output for text in ["ImportError", "ModuleNotFoundError", "SyntaxError", "IndentationError", "NameError"]):
        events.append(("Test module setup/import", "execution_error"))
    return events


def decode_subprocess_output(output: bytes | None) -> str:
    if not output:
        return ""
    try:
        return output.decode("utf-8")
    except UnicodeDecodeError:
        return output.decode("cp1252", errors="replace")


def run_one_combination(task: int, run: int, test_source: str, implementation_source: str) -> dict:
    test_file = get_test_file(task, run, test_source)
    implementation_file = get_implementation_file(task, run, implementation_source)
    pairing_name = f"task_{task}_run_{run:02d}__tests_{test_source}__implementation_{implementation_source}"
    pairing_work_dir = WORK_DIR / pairing_name
    log_file = LOG_DIR / f"{pairing_name}.txt"
    shutil.rmtree(pairing_work_dir, ignore_errors=True)
    pairing_work_dir.mkdir(parents=True, exist_ok=True)
    missing_items = []
    if not test_file.exists():
        missing_items.append(f"Missing test file:\n{test_file}")
    if not implementation_file.exists():
        missing_items.append(f"Missing implementation file:\n{implementation_file}")
    if missing_items:
        output = "\n\n".join(missing_items)
        log_file.write_text(output, encoding="utf-8")
        return {"test_file": test_file, "implementation_file": implementation_file, "return_code": -1, "output": output, "passed": 0, "failed": 0, "errors": 1, "skipped": 0, "total": 0, "log_file": log_file}
    shutil.copy2(implementation_file, pairing_work_dir / "implementation_manual.py")
    shutil.copy2(test_file, pairing_work_dir / "selected_test.py")
    command = [sys.executable, "-m", "unittest", "-v", "selected_test"]
    try:
        completed_process = subprocess.run(command, cwd=pairing_work_dir, capture_output=True, text=False, timeout=TIMEOUT_SECONDS)
        stdout_output = decode_subprocess_output(completed_process.stdout)
        stderr_output = decode_subprocess_output(completed_process.stderr)
        output = (f"Command: {' '.join(command)}\nTimestamp: {datetime.now().isoformat(timespec='seconds')}\nReturn code: {completed_process.returncode}\n{'=' * 80}\n\nSTANDARD OUTPUT\n{'-' * 80}\n{stdout_output}\n\nSTANDARD ERROR\n{'-' * 80}\n{stderr_output}")
        return_code = completed_process.returncode
    except subprocess.TimeoutExpired as timeout_error:
        stdout_output = decode_subprocess_output(timeout_error.stdout)
        stderr_output = decode_subprocess_output(timeout_error.stderr)
        output = (f"Execution timed out after {TIMEOUT_SECONDS} seconds.\n\nCommand: {' '.join(command)}\n\nTest file:\n{test_file}\n\nImplementation file:\n{implementation_file}\n\nSTANDARD OUTPUT BEFORE TIMEOUT\n{'-' * 80}\n{stdout_output}\n\nSTANDARD ERROR BEFORE TIMEOUT\n{'-' * 80}\n{stderr_output}")
        return_code = -2
    log_file.write_text(output, encoding="utf-8")
    counts = parse_unittest_output(output)
    if return_code != 0 and counts["total"] == 0:
        counts["errors"] = 1
    return {"test_file": test_file, "implementation_file": implementation_file, "return_code": return_code, "output": output, "passed": counts["passed"], "failed": counts["failed"], "errors": counts["errors"], "skipped": counts["skipped"], "total": counts["total"], "log_file": log_file}


def main() -> None:
    if TASK_NUMBER not in MANUAL_TASK_FOLDERS:
        raise ValueError("TASK_NUMBER must be a number from 1 to 9.")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    if OVERWRITE_PREVIOUS_RESULTS:
        MATRIX_CSV.unlink(missing_ok=True)
        FAILED_TESTS_CSV.unlink(missing_ok=True)
    create_csv_if_missing(MATRIX_CSV, MATRIX_HEADERS)
    create_csv_if_missing(FAILED_TESTS_CSV, FAILED_TEST_HEADERS)
    completed_combinations = load_completed_combinations()
    selected_runs = [1] if PILOT_MODE else list(RUNS)
    total_combinations = len(selected_runs) * len(ALL_SOURCES) * len(ALL_SOURCES)
    executed_count = 0
    skipped_count = 0
    print("\n" + "=" * 78)
    print(f"TASK {TASK_NUMBER}: CROSS-EVALUATION MATRIX")
    print("=" * 78)
    print(f"Runs selected: {selected_runs}")
    print(f"Expected combinations: {total_combinations}")
    print(f"Matrix CSV: {MATRIX_CSV}")
    print(f"Individual-failure CSV: {FAILED_TESTS_CSV}")
    print("=" * 78 + "\n")
    for run in selected_runs:
        print(f"\n--- TASK {TASK_NUMBER}, RUN {run:02d} ---\n")
        for test_source in ALL_SOURCES:
            for implementation_source in ALL_SOURCES:
                combination_key = (str(run), test_source, implementation_source)
                if combination_key in completed_combinations:
                    skipped_count += 1
                    print(f"SKIP | Run {run:02d} | {test_source:8} tests vs {implementation_source:8} implementation")
                    continue
                executed_count += 1
                print(f"RUN  | Run {run:02d} | {test_source:8} tests vs {implementation_source:8} implementation")
                result = run_one_combination(TASK_NUMBER, run, test_source, implementation_source)
                complete = result["return_code"] == 0 and result["total"] > 0 and result["failed"] == 0 and result["errors"] == 0
                matrix_row = {"task": TASK_NUMBER, "run": run, "test_source": test_source, "implementation_source": implementation_source, "test_file": str(result["test_file"]), "implementation_file": str(result["implementation_file"]), "passed_tests": result["passed"], "failed_tests": result["failed"], "error_tests": result["errors"], "skipped_tests": result["skipped"], "total_tests": result["total"], "complete": "Yes" if complete else "No", "return_code": result["return_code"], "log_file": str(result["log_file"]), "investigation_status": "Not required" if complete else "To investigate", "failure_cause": "", "error_category": "", "manual_notes": ""}
                append_csv_row(MATRIX_CSV, MATRIX_HEADERS, matrix_row)
                if not complete:
                    failure_events = get_failed_test_events(result["output"]) or [("Unidentified execution issue", "error")]
                    for test_name, result_type in failure_events:
                        append_csv_row(FAILED_TESTS_CSV, FAILED_TEST_HEADERS, {"task": TASK_NUMBER, "run": run, "test_source": test_source, "implementation_source": implementation_source, "test_name": test_name, "result_type": result_type, "log_file": str(result["log_file"]), "failure_cause": "", "error_category": "", "manual_notes": ""})
                print(f"       Passed {result['passed']}/{result['total']} | Failed {result['failed']} | Errors {result['errors']} | Skipped {result['skipped']} | Complete: {'Yes' if complete else 'No'}\n")
    create_review_sheet()
    print("\n" + "=" * 78)
    print("EXECUTION FINISHED")
    print("=" * 78)
    print(f"New combinations executed: {executed_count}")
    print(f"Existing combinations skipped: {skipped_count}")
    print(f"Matrix CSV: {MATRIX_CSV}")
    print(f"Readable review CSV: {REVIEW_CSV}")
    print(f"Failure CSV: {FAILED_TESTS_CSV}")
    print(f"Traceback logs: {LOG_DIR}")
    print("=" * 78 + "\n")


if __name__ == "__main__":
    main()
