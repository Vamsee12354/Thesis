from __future__ import annotations

import csv
import re
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path


# ============================================================
# SETTINGS — CHANGE ONLY THESE VALUES
# ============================================================

TASK_NUMBER = 7

# False = execute all runs 01–10, skipping matrix rows already saved.
# True = execute Run 01 only, useful for a small pilot.
PILOT_MODE = False

# False = preserve existing CSV rows and skip those combinations.
# True = delete the Task CSVs and run all selected combinations again.
OVERWRITE_PREVIOUS_RESULTS = True

# Maximum time allowed for one test-suite / implementation pairing.
TIMEOUT_SECONDS = 600


# ============================================================
# PROJECT CONFIGURATION
# ============================================================

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

MATRIX_HEADERS = [
    "task",
    "run",
    "test_source",
    "implementation_source",
    "test_file",
    "implementation_file",
    "passed_tests",
    "failed_tests",
    "error_tests",
    "skipped_tests",
    "total_tests",
    "complete",
    "return_code",
    "log_file",
    "investigation_status",
    "failure_cause",
    "error_category",
    "manual_notes",
]

FAILED_TEST_HEADERS = [
    "task",
    "run",
    "test_source",
    "implementation_source",
    "test_name",
    "result_type",
    "log_file",
    "failure_cause",
    "error_category",
    "manual_notes",
]

REVIEW_HEADERS = [
    "Run",
    "Test LLM",
    "Implementation LLM",
    "Passed tests",
    "Total Tests",
    "Complete?",
    "Notes",
]


# ============================================================
# FIND INPUT FILES
# ============================================================

def get_test_file(task: int, run: int, test_source: str) -> Path:
    """Return the test-suite file for one source in one run."""
    if test_source == "manual":
        return (
            BASE_DIR
            / "src"
            / MANUAL_TASK_FOLDERS[task]
            / "tests.py"
        )

    return (
        BASE_DIR
        / "generated_tests"
        / test_source
        / f"task_{task}"
        / f"run_{run:02d}_test.py"
    )


def get_implementation_file(
    task: int,
    run: int,
    implementation_source: str,
) -> Path:
    """Return the implementation file for one source in one run."""
    if implementation_source == "manual":
        return (
            BASE_DIR
            / "src"
            / MANUAL_TASK_FOLDERS[task]
            / "implementation_manual.py"
        )

    return (
        BASE_DIR
        / "results"
        / implementation_source
        / f"task_{task}"
        / f"run_{run:02d}.py"
    )


# ============================================================
# CSV FUNCTIONS
# ============================================================

def create_csv_if_missing(path: Path, headers: list[str]) -> None:
    """Create a CSV with headers only if it does not already exist."""
    if not path.exists():
        with path.open("w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=headers)
            writer.writeheader()


def append_csv_row(path: Path, headers: list[str], row: dict) -> None:
    """Append one result row to a CSV."""
    with path.open("a", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writerow(row)


def load_completed_combinations() -> set[tuple[str, str, str]]:
    """
    Read existing matrix results.

    A combination is identified by:
    (run, test_source, implementation_source).
    """
    completed = set()

    if OVERWRITE_PREVIOUS_RESULTS or not MATRIX_CSV.exists():
        return completed

    with MATRIX_CSV.open("r", newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            completed.add((
                row["run"],
                row["test_source"],
                row["implementation_source"],
            ))

    return completed


def create_review_sheet() -> None:
    """
    Create a readable CSV for manual investigation.

    It preserves the raw matrix CSV unchanged, but creates blank rows
    between each Test LLM block and two blank rows between runs.
    """
    if not MATRIX_CSV.exists():
        return

    display_names = {
        "deepseek": "Deepseek",
        "gemma": "Gemma",
        "mistral": "Mistral",
        "openai": "OpenAI",
        "amazon": "Amazon",
        "manual": "Manual",
    }

    matrix_rows = []

    with MATRIX_CSV.open("r", newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        matrix_rows = list(reader)

    with REVIEW_CSV.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=REVIEW_HEADERS)
        writer.writeheader()

        for run in sorted({int(row["run"]) for row in matrix_rows if row["run"]}):
            run_rows = [
                row
                for row in matrix_rows
                if row["run"] == str(run)
            ]

            for test_source in ALL_SOURCES:
                suite_rows = [
                    row
                    for row in run_rows
                    if row["test_source"] == test_source
                ]

                suite_rows.sort(
                    key=lambda row: ALL_SOURCES.index(
                        row["implementation_source"]
                    )
                )

                for row in suite_rows:
                    notes = ""

                    if row["complete"] == "No":
                        notes = "To investigate"

                    writer.writerow({
                        "Run": row["run"],
                        "Test LLM": display_names[
                            row["test_source"]
                        ],
                        "Implementation LLM": display_names[
                            row["implementation_source"]
                        ],
                        "Passed tests": row["passed_tests"],
                        "Total Tests": row["total_tests"],
                        "Complete?": row["complete"],
                        "Notes": notes,
                    })

                # One blank row after each Test LLM block.
                writer.writerow({
                    "Run": "",
                    "Test LLM": "",
                    "Implementation LLM": "",
                    "Passed tests": "",
                    "Total Tests": "",
                    "Complete?": "",
                    "Notes": "",
                })

            # A second blank row between complete runs.
            writer.writerow({
                "Run": "",
                "Test LLM": "",
                "Implementation LLM": "",
                "Passed tests": "",
                "Total Tests": "",
                "Complete?": "",
                "Notes": "",
            })


# ============================================================
# UNITTEST OUTPUT PARSING
# ============================================================

def parse_unittest_output(output: str) -> dict:
    """Extract pass/fail/error/skip totals from unittest terminal output."""
    total_match = re.search(
        r"Ran\s+(\d+)\s+test(?:s)?",
        output,
        flags=re.IGNORECASE,
    )

    failures_match = re.search(
        r"failures=(\d+)",
        output,
        flags=re.IGNORECASE,
    )

    errors_match = re.search(
        r"errors=(\d+)",
        output,
        flags=re.IGNORECASE,
    )

    skipped_match = re.search(
        r"skipped=(\d+)",
        output,
        flags=re.IGNORECASE,
    )

    total = int(total_match.group(1)) if total_match else 0
    failures = int(failures_match.group(1)) if failures_match else 0
    errors = int(errors_match.group(1)) if errors_match else 0
    skipped = int(skipped_match.group(1)) if skipped_match else 0

    passed = max(total - failures - errors - skipped, 0)

    return {
        "passed": passed,
        "failed": failures,
        "errors": errors,
        "skipped": skipped,
        "total": total,
    }


def get_failed_test_events(output: str) -> list[tuple[str, str]]:
    """
    Extract individual test names reported as FAIL or ERROR.

    If the entire suite fails at import/setup time, add one event
    called 'Test module setup/import'.
    """
    events = []

    test_result_pattern = (
        r"^(.+?)\s+\((.+?)\)\s+\.\.\.\s+"
        r"(FAIL|ERROR|UNEXPECTED SUCCESS)$"
    )

    for line in output.splitlines():
        match = re.match(test_result_pattern, line.strip())

        if match:
            short_name = match.group(1)
            full_name = match.group(2)
            result_type = match.group(3).lower().replace(" ", "_")

            events.append((
                f"{short_name} ({full_name})",
                result_type,
            ))

    if not events and any(
        error_text in output
        for error_text in [
            "ImportError",
            "ModuleNotFoundError",
            "SyntaxError",
            "IndentationError",
            "NameError",
        ]
    ):
        events.append((
            "Test module setup/import",
            "execution_error",
        ))

    return events


# ============================================================
# EXECUTE ONE PAIRING IN A CLEAN FOLDER
# ============================================================

def run_one_combination(
    task: int,
    run: int,
    test_source: str,
    implementation_source: str,
) -> dict:
    """
    Run one test-suite / implementation combination.

    Both source files are copied into a new temporary folder.
    The selected implementation is always renamed to
    implementation_manual.py because the test suites import that name.
    """
    test_file = get_test_file(task, run, test_source)

    implementation_file = get_implementation_file(
        task,
        run,
        implementation_source,
    )

    pairing_name = (
        f"task_{task}_run_{run:02d}"
        f"__tests_{test_source}"
        f"__implementation_{implementation_source}"
    )

    pairing_work_dir = WORK_DIR / pairing_name
    log_file = LOG_DIR / f"{pairing_name}.txt"

    shutil.rmtree(pairing_work_dir, ignore_errors=True)
    pairing_work_dir.mkdir(parents=True, exist_ok=True)

    missing_items = []

    if not test_file.exists():
        missing_items.append(f"Missing test file:\n{test_file}")

    if not implementation_file.exists():
        missing_items.append(
            f"Missing implementation file:\n{implementation_file}"
        )

    if missing_items:
        output = "\n\n".join(missing_items)
        log_file.write_text(output, encoding="utf-8")

        return {
            "test_file": test_file,
            "implementation_file": implementation_file,
            "return_code": -1,
            "output": output,
            "passed": 0,
            "failed": 0,
            "errors": 1,
            "skipped": 0,
            "total": 0,
            "log_file": log_file,
        }

    shutil.copy2(
        implementation_file,
        pairing_work_dir / "implementation_manual.py",
    )

    shutil.copy2(
        test_file,
        pairing_work_dir / "selected_test.py",
    )

    command = [
        sys.executable,
        "-m",
        "unittest",
        "-v",
        "selected_test",
    ]

    try:
        completed_process = subprocess.run(
            command,
            cwd=pairing_work_dir,
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=TIMEOUT_SECONDS,
        )

        output = (
            f"Command: {' '.join(command)}\n"
            f"Timestamp: {datetime.now().isoformat(timespec='seconds')}\n"
            f"Return code: {completed_process.returncode}\n"
            f"{'=' * 80}\n\n"
            f"STANDARD OUTPUT\n"
            f"{'-' * 80}\n"
            f"{completed_process.stdout}\n\n"
            f"STANDARD ERROR\n"
            f"{'-' * 80}\n"
            f"{completed_process.stderr}"
        )

        return_code = completed_process.returncode

    except subprocess.TimeoutExpired:
        output = (
            f"Execution timed out after {TIMEOUT_SECONDS} seconds.\n\n"
            f"Test file:\n{test_file}\n\n"
            f"Implementation file:\n{implementation_file}\n"
        )

        return_code = -2

    log_file.write_text(output, encoding="utf-8")

    counts = parse_unittest_output(output)

    # A failed setup/import can result in no recognised test count,
    # but still needs to be recorded as an execution error.
    if return_code != 0 and counts["total"] == 0:
        counts["errors"] = 1

    return {
        "test_file": test_file,
        "implementation_file": implementation_file,
        "return_code": return_code,
        "output": output,
        "passed": counts["passed"],
        "failed": counts["failed"],
        "errors": counts["errors"],
        "skipped": counts["skipped"],
        "total": counts["total"],
        "log_file": log_file,
    }


# ============================================================
# RUN FULL MATRIX
# ============================================================

def main() -> None:
    if TASK_NUMBER not in MANUAL_TASK_FOLDERS:
        raise ValueError("TASK_NUMBER must be a number from 1 to 9.")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    LOG_DIR.mkdir(parents=True, exist_ok=True)

    # This option starts the selected task again from scratch.
    if OVERWRITE_PREVIOUS_RESULTS:
        MATRIX_CSV.unlink(missing_ok=True)
        FAILED_TESTS_CSV.unlink(missing_ok=True)

    create_csv_if_missing(MATRIX_CSV, MATRIX_HEADERS)
    create_csv_if_missing(FAILED_TESTS_CSV, FAILED_TEST_HEADERS)

    completed_combinations = load_completed_combinations()

    selected_runs = [1] if PILOT_MODE else list(RUNS)

    total_combinations = (
        len(selected_runs)
        * len(ALL_SOURCES)
        * len(ALL_SOURCES)
    )

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
                combination_key = (
                    str(run),
                    test_source,
                    implementation_source,
                )

                if combination_key in completed_combinations:
                    skipped_count += 1

                    print(
                        f"SKIP | Run {run:02d} | "
                        f"{test_source:8} tests vs "
                        f"{implementation_source:8} implementation"
                    )

                    continue

                executed_count += 1

                print(
                    f"RUN  | Run {run:02d} | "
                    f"{test_source:8} tests vs "
                    f"{implementation_source:8} implementation"
                )

                result = run_one_combination(
                    task=TASK_NUMBER,
                    run=run,
                    test_source=test_source,
                    implementation_source=implementation_source,
                )

                # Skips are recorded but are not automatically failures.
                complete = (
                    result["return_code"] == 0
                    and result["total"] > 0
                    and result["failed"] == 0
                    and result["errors"] == 0
                )

                matrix_row = {
                    "task": TASK_NUMBER,
                    "run": run,
                    "test_source": test_source,
                    "implementation_source": implementation_source,
                    "test_file": str(result["test_file"]),
                    "implementation_file": str(
                        result["implementation_file"]
                    ),
                    "passed_tests": result["passed"],
                    "failed_tests": result["failed"],
                    "error_tests": result["errors"],
                    "skipped_tests": result["skipped"],
                    "total_tests": result["total"],
                    "complete": "Yes" if complete else "No",
                    "return_code": result["return_code"],
                    "log_file": str(result["log_file"]),
                    "investigation_status": (
                        "Not required"
                        if complete
                        else "To investigate"
                    ),
                    "failure_cause": "",
                    "error_category": "",
                    "manual_notes": "",
                }

                append_csv_row(
                    MATRIX_CSV,
                    MATRIX_HEADERS,
                    matrix_row,
                )

                if not complete:
                    failure_events = get_failed_test_events(
                        result["output"]
                    )

                    if not failure_events:
                        failure_events = [
                            ("Unidentified execution issue", "error")
                        ]

                    for test_name, result_type in failure_events:
                        failure_row = {
                            "task": TASK_NUMBER,
                            "run": run,
                            "test_source": test_source,
                            "implementation_source": implementation_source,
                            "test_name": test_name,
                            "result_type": result_type,
                            "log_file": str(result["log_file"]),
                            "failure_cause": "",
                            "error_category": "",
                            "manual_notes": "",
                        }

                        append_csv_row(
                            FAILED_TESTS_CSV,
                            FAILED_TEST_HEADERS,
                            failure_row,
                        )

                print(
                    f"       Passed {result['passed']}/{result['total']} | "
                    f"Failed {result['failed']} | "
                    f"Errors {result['errors']} | "
                    f"Skipped {result['skipped']} | "
                    f"Complete: {'Yes' if complete else 'No'}\n"
                )

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