from __future__ import annotations
import argparse
import collections
import concurrent.futures
import csv
import datetime as dt
import hashlib
import importlib
import importlib.metadata
import json
import os
from pathlib import Path
import platform
import shutil
import signal
import statistics
import subprocess
import sys
import time
import traceback
import uuid


VERSION = "1.0.1"
# This patch changes file checkpoint handling, not measurement/counting rules.
# Accept unchanged case caches from the exact preceding release.
COMPATIBLE_SIGNATURES = (("1.0", "ee5b2663e9d837825bbc187094fe8012779de4f4c57ed1b9d3ac735ba794f92e"),)
LLMS = ("manual", "openai", "deepseek", "gemma", "Mistral", "amazon")
TASK_FOLDERS = {
    1: "task1_unique_brands", 2: "task2_get_average_price",
    3: "task3_get_min_attribute", 4: "task4_get_reading_duration",
    5: "task5_validate_contact_form", 6: "task6_validate_password",
    7: "task7_product_list_live_v", 8: "task8_slugify",
    9: "task9_product_cache_get",
}
# Preserved from your supplied script. Change here if your thesis rubric differs.
COMPLEXITY = {1: "Low", 2: "Low", 3: "Low", 4: "Medium", 5: "Medium",
              6: "Medium", 7: "High", 8: "Medium", 9: "High"}
COUNT_FIELDS = ("tests_run", "tests_passed", "tests_failed", "tests_errored",
                "tests_skipped", "expected_failures", "unexpected_successes")
GOOD_EXECUTIONS = {"completed", "tests_failed"}
OWNED_LOCK = None


def release_run_lock():
    if OWNED_LOCK is not None:
        path, owner = OWNED_LOCK
        try:
            if path.read_text(encoding="utf-8") == owner:
                path.unlink()
        except FileNotFoundError:
            pass


def atomic_json(path, value):
    path = Path(path)
    tmp = path.with_name(path.name + "." + uuid.uuid4().hex + ".tmp")
    payload = json.dumps(value, ensure_ascii=False, indent=2)
    for attempt in range(6):
        try:
            tmp.write_text(payload, encoding="utf-8")
            os.replace(tmp, path)
            return
        except PermissionError:
            if attempt == 5:
                raise
            time.sleep(0.02 * 2 ** attempt)


def stamp():
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def case_child():
    """Internal worker. Never call directly from the terminal."""
    import unittest
    import coverage

    folder = Path.cwd()
    spec = json.loads((folder / "case.json").read_text(encoding="utf-8"))
    impl = folder / "implementation_manual.py"
    target = str(impl.resolve())
    started = time.perf_counter()
    result = {**{k: None for k in COUNT_FIELDS}, "counts_complete": False,
              "coverage_pct": None, "lines_covered": None, "lines_total": None,
              "lines_missing": None, "eligible": False, "status": "worker_error",
              "error_detail": "", "started_utc": stamp(),
              "python": sys.version, "coverage_version": coverage.__version__}
    # Selected case imports must take precedence over the original project.
    sys.path.insert(0, str(folder))
    sys.dont_write_bytecode = True

    class CountingResult(unittest.TextTestResult):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.case_states = []
            self.active = None
            self.fixture_errors = []
            self.subtest_failures = 0
            self.subtest_errors = 0

        def startTest(self, test):
            self.active = {"id": test.id(), "outcome": "passed", "complete": False}
            self.case_states.append(self.active)
            super().startTest(test)

        def mark(self, test, outcome):
            if self.active is None:
                self.fixture_errors.append(str(test))
                return
            current = self.active["outcome"]
            # Disjoint per-test outcomes; an error takes precedence over a failure.
            priority = {"passed": 0, "skipped": 1, "expected_failure": 1,
                        "unexpected_success": 2, "failed": 3, "errored": 4}
            if priority[outcome] >= priority[current]:
                self.active["outcome"] = outcome

        def addSuccess(self, test):
            self.mark(test, "passed")
            super().addSuccess(test)

        def addFailure(self, test, err):
            self.mark(test, "failed")
            super().addFailure(test, err)

        def addError(self, test, err):
            self.mark(test, "errored")
            super().addError(test, err)

        def addSkip(self, test, reason):
            # A skipped subtest does not make the whole parent a skipped test.
            if not hasattr(test, "test_case"):
                self.mark(test, "skipped")
            super().addSkip(test, reason)

        def addExpectedFailure(self, test, err):
            self.mark(test, "expected_failure")
            super().addExpectedFailure(test, err)

        def addUnexpectedSuccess(self, test):
            self.mark(test, "unexpected_success")
            super().addUnexpectedSuccess(test)

        def addSubTest(self, test, subtest, err):
            if err is not None:
                failure = issubclass(err[0], test.failureException)
                self.mark(test, "failed" if failure else "errored")
                if failure:
                    self.subtest_failures += 1
                else:
                    self.subtest_errors += 1
            super().addSubTest(test, subtest, err)

        def counts(self):
            states = collections.Counter(s["outcome"] for s in self.case_states if s["complete"])
            return {"tests_run": sum(states.values()), "tests_passed": states["passed"],
                    "tests_failed": states["failed"], "tests_errored": states["errored"],
                    "tests_skipped": states["skipped"],
                    "expected_failures": states["expected_failure"],
                    "unexpected_successes": states["unexpected_success"]}

        def stopTest(self, test):
            if self.active is not None:
                self.active["complete"] = True
            super().stopTest(test)
            self.active = None
            # Counts live in memory. A locked optional checkpoint must not abort
            # unittest or turn collected coverage into a partial measurement.
            if not result.get("checkpoint_warning"):
                try:
                    atomic_json(folder / "progress.json", {**self.counts(), "complete": False})
                except OSError as exc:
                    result["checkpoint_warning"] = str(exc)
                    print(f"Progress checkpoint unavailable; tests continue: {exc}", file=sys.stderr)

    cov = coverage.Coverage(data_file=str(folder / ".coverage"),
                            config_file=False, include=[target], branch=False)
    cov_started = False
    test_result = None
    try:
        for filename, status in [(impl, "implementation_syntax_error"),
                                 (folder / "test_module.py", "test_syntax_error")]:
            try:
                compile(filename.read_bytes(), str(filename), "exec")
            except (SyntaxError, UnicodeError):
                result["status"] = status
                raise
        cov.start()
        cov_started = True
        result["status"] = "test_import_error"
        module = importlib.import_module("test_module")
        loader = unittest.TestLoader()
        result["status"] = "test_load_error"
        suite = loader.loadTestsFromModule(module)
        if loader.errors:
            raise RuntimeError("\n".join(loader.errors))
        result["status"] = "test_runner_error"
        runner = unittest.TextTestRunner(stream=sys.stderr, verbosity=2,
                                         resultclass=CountingResult)
        test_result = runner.run(suite)
        result.update(test_result.counts())
        result["counts_complete"] = True
        result["unittest_tests_run"] = test_result.testsRun
        result["subtest_failure_events"] = test_result.subtest_failures
        result["subtest_error_events"] = test_result.subtest_errors
        result["case_outcomes"] = test_result.case_states
        if test_result.fixture_errors:
            result["status"] = "test_fixture_error"
            result["error_detail"] = "Class/module fixture errors: " + "; ".join(test_result.fixture_errors)
        elif test_result.testsRun == 0:
            result["status"] = "no_tests"
            result["error_detail"] = "The selected suite discovered zero test cases."
        else:
            result["status"] = "completed" if test_result.wasSuccessful() else "tests_failed"
    except BaseException:
        result["error_detail"] = traceback.format_exc()
        print(result["error_detail"], file=sys.stderr)
    finally:
        if cov_started:
            try:
                cov.stop()
                cov.save()
                data = cov.get_data()
                measured = {os.path.normcase(str(Path(p).resolve())) for p in data.measured_files()}
                if os.path.normcase(target) in measured:
                    _, statements, excluded, missing, _ = cov.analysis2(target)
                    total = len(statements)
                    covered = total - len(missing)
                    result.update(lines_total=total, lines_missing=len(missing), lines_covered=covered)
                    result["coverage_pct"] = 100.0 * covered / total if total else None
                    result["missing_line_numbers"] = missing
                    result["excluded_line_numbers"] = excluded
                    cov.json_report(morfs=[target], outfile=str(folder / "coverage.json"))
                elif result["status"] in GOOD_EXECUTIONS:
                    result["error_detail"] = "Tests completed but did not execute the selected implementation."
                    result["status"] = "implementation_not_executed"
            except BaseException:
                result["coverage_error"] = traceback.format_exc()
                if result["status"] in GOOD_EXECUTIONS:
                    result["status"] = "coverage_error"
                    result["error_detail"] = result["coverage_error"]
            if result["status"] in GOOD_EXECUTIONS and result["coverage_pct"] is None:
                result["status"] = "no_executable_lines"
                result["error_detail"] = "No measurable executable implementation statements."
        result["eligible"] = (result["status"] in GOOD_EXECUTIONS and
                              result["counts_complete"] and bool(result["tests_run"]) and
                              result["coverage_pct"] is not None)
        result["elapsed_seconds"] = round(time.perf_counter() - started, 4)
        result["finished_utc"] = stamp()
        atomic_json(folder / "worker_result.json", result)
    # Do not wait for stray non-daemon cache Timer threads after the suite ends.
    sys.stdout.flush()
    sys.stderr.flush()
    os._exit(0)


def matching_child(parent, wanted):
    exact = parent / wanted
    if exact.exists() or not parent.is_dir():
        return exact
    matches = [p for p in parent.iterdir() if p.name.casefold() == wanted.casefold()]
    if len(matches) > 1:
        raise ValueError(f"Ambiguous directory spelling under {parent}: {wanted}")
    return matches[0] if matches else exact


def paths_for(base, task, run, llm, is_test):
    if llm == "manual":
        return base / "src" / TASK_FOLDERS[task] / ("tests.py" if is_test else "implementation_manual.py")
    tree = base / ("generated_tests" if is_test else "results")
    source = matching_child(tree, llm)
    name = f"run_{run:02d}_test.py" if is_test else f"run_{run:02d}.py"
    return source / f"task_{task}" / name


def stop_process(process):
    if process.poll() is not None:
        return
    if os.name == "nt":
        subprocess.run(["taskkill", "/PID", str(process.pid), "/T", "/F"],
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
    else:
        try:
            os.killpg(process.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
    try:
        process.wait(timeout=5)
    except subprocess.TimeoutExpired:
        process.kill()
        process.wait()


def measure_job(job, config, children, lock):
    key = job["key"]
    root = config["out"] / "evidence" / key
    latest = root / "latest.json"
    fingerprint = job["fingerprint"]
    if latest.is_file() and not config["fresh"]:
        try:
            saved = json.loads(latest.read_text(encoding="utf-8"))
            checkpoint_error = (saved.get("status") == "test_runner_error" and
                                "progress.json" in saved.get("error_detail", "") and
                                "PermissionError" in saved.get("error_detail", ""))
            retry = (saved.get("status") == "interrupted" or
                     (config["retry_errors"] and not saved.get("eligible", False)) or
                     (config.get("retry_checkpoint_errors", False) and checkpoint_error))
            accepted = [fingerprint] + job.get("compatible_fingerprints", [])
            if saved.get("fingerprint") in accepted and not retry:
                saved["reused"] = True
                return saved
        except (OSError, ValueError):
            pass
    root.mkdir(parents=True, exist_ok=True)
    attempt = root / (dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%S") + "_" + uuid.uuid4().hex[:8])
    attempt.mkdir()
    record = {k: v for k, v in job.items() if k not in ("impl_path", "test_path", "compatible_fingerprints")}
    record.update({k: None for k in COUNT_FIELDS})
    record.update(coverage_pct=None, lines_covered=None, lines_total=None,
                  lines_missing=None, eligible=False, counts_complete=False,
                  status="execution_error", error_detail="", reused=False,
                  evidence=str(attempt.relative_to(config["out"])), started_utc=stamp())
    atomic_json(attempt / "case.json", {"task": job["task"], "run": job["run"],
                 "implementation": str(job["impl_path"]), "test": str(job["test_path"]),
                 "fingerprint": fingerprint, "timeout": config["timeout"]})
    started = time.perf_counter()
    process = None
    try:
        for src, dst in [(job["impl_path"], "implementation_manual.py"),
                         (job["test_path"], "test_module.py")]:
            if not src.is_file():
                record["status"] = "missing_implementation" if dst.startswith("implementation") else "missing_test"
                raise FileNotFoundError(f"Required source file is missing: {src}")
            shutil.copyfile(src, attempt / dst)
        # Support either import form without rewriting the submitted tests:
        # from implementation_manual import ...
        # from src.taskN_name.implementation_manual import ...
        package = attempt / "src" / TASK_FOLDERS[job["task"]]
        package.mkdir(parents=True)
        (package.parent / "__init__.py").write_text("", encoding="utf-8")
        (package / "__init__.py").write_text("", encoding="utf-8")
        (package / "implementation_manual.py").write_text(
            'import importlib, sys\nsys.modules[__name__] = importlib.import_module("implementation_manual")\n',
            encoding="utf-8")
        env = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONDONTWRITEBYTECODE="1")
        kwargs = {"creationflags": subprocess.CREATE_NEW_PROCESS_GROUP} if os.name == "nt" else {"start_new_session": True}
        with (attempt / "stdout.txt").open("w", encoding="utf-8") as stdout, \
             (attempt / "stderr.txt").open("w", encoding="utf-8") as stderr:
            with lock:
                if config["stop_event"].is_set():
                    raise InterruptedError("Run interrupted before this worker started.")
                process = subprocess.Popen([sys.executable, str(config["script"]), "--_worker"],
                                           cwd=attempt, stdout=stdout, stderr=stderr, env=env, **kwargs)
                children.add(process)
            try:
                process.wait(timeout=config["timeout"])
            except subprocess.TimeoutExpired:
                record["status"] = "timeout"
                record["error_detail"] = f"Test execution exceeded {config['timeout']:g} seconds. Counts are incomplete."
                stop_process(process)
        worker_file = attempt / "worker_result.json"
        if worker_file.is_file():
            record.update(json.loads(worker_file.read_text(encoding="utf-8")))
        elif config["stop_event"].is_set():
            record["status"] = "interrupted"
            record["error_detail"] = "Execution interrupted. This combination will be retried automatically."
        elif record["status"] != "timeout":
            record["error_detail"] = f"Worker exited without a result (return code {process.returncode}). See stderr.txt."
        progress = attempt / "progress.json"
        if record["status"] == "timeout" and progress.is_file():
            record["partial_test_counts"] = json.loads(progress.read_text(encoding="utf-8"))
        record["return_code"] = process.returncode
    except Exception:
        if config["stop_event"].is_set():
            record["status"] = "interrupted"
        elif record["status"] == "execution_error":
            record["status"] = "runner_error"
        record["error_detail"] = traceback.format_exc()
    finally:
        if process is not None:
            stop_process(process)
            with lock:
                children.discard(process)
    record["elapsed_seconds"] = round(time.perf_counter() - started, 4)
    record["finished_utc"] = stamp()
    atomic_json(attempt / "result.json", record)
    atomic_json(latest, record)
    return record


def row_values(record):
    return [record[k] for k in ("task", "task_name", "complexity", "run", "impl_llm", "test_llm",
             "coverage_pct", "lines_covered", "lines_total", "lines_missing",
             "tests_run", "tests_passed", "tests_failed", "tests_errored", "tests_skipped",
             "status", "eligible", "counts_complete")]


HEADERS = ["Task", "Task Name", "Complexity", "Run", "Impl LLM", "Test LLM",
           "Coverage %", "Lines Covered", "Lines Total", "Lines Missing", "Tests Run",
           "Tests Passed", "Tests Failed", "Tests Errored", "Tests Skipped", "Status",
           "Use in Averages", "Test Counts Complete"]


def export_results(records, out):
    """Keep the original Python/openpyxl reporting stack, with plain formatting."""
    import openpyxl
    from openpyxl.styles import Font
    from openpyxl.utils import get_column_letter

    records = sorted(records, key=lambda r: (r["task"], r["run"], LLMS.index(r["impl_llm"]), LLMS.index(r["test_llm"])))
    extra_outcomes = any(r.get("expected_failures") or r.get("unexpected_successes") for r in records)
    headers = HEADERS + (["Expected Failures", "Unexpected Successes"] if extra_outcomes else [])

    def output_row(r):
        return row_values(r) + ([r.get("expected_failures"), r.get("unexpected_successes")] if extra_outcomes else [])

    csv_tmp = out / "measurements.csv.tmp"
    with csv_tmp.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.writer(handle)
        writer.writerow(headers)
        writer.writerows(output_row(r) for r in records)
    os.replace(csv_tmp, out / "measurements.csv")
    wb = openpyxl.Workbook()
    detail = wb.active
    detail.title = "All Measurements"
    detail.append(headers)
    for record in records:
        detail.append(output_row(record))
    pair = wb.create_sheet("Mean by LLM Pair")
    pair.append(["Task", "Task Name", "Complexity", "Impl LLM", "Test LLM", "Mean Coverage %",
                 "Std Dev", "Min %", "Max %", "Measurements Used", "Total Attempts"])
    groups = collections.defaultdict(list)
    complexity_groups = collections.defaultdict(list)
    for r in records:
        groups[(r["task"], r["impl_llm"], r["test_llm"])].append(r)
        complexity_groups[(r["complexity"], r["test_llm"])].append(r)

    def stats(group):
        values = [r["coverage_pct"] for r in group if r["eligible"]]
        if not values:
            return [None, None, None, None, 0]
        return [round(statistics.mean(values), 4),
                round(statistics.stdev(values), 4) if len(values) > 1 else 0,
                min(values), max(values), len(values)]

    for (task, impl, tests), group in sorted(groups.items()):
        pair.append([task, TASK_FOLDERS[task], COMPLEXITY[task], impl, tests, *stats(group), len(group)])
    complexity = wb.create_sheet("Mean by Test and Complexity")
    complexity.append(["Complexity", "Test LLM", "Mean Coverage %", "Std Dev", "Min %", "Max %", "Measurements Used"])
    for (tier, tests), group in sorted(complexity_groups.items()):
        complexity.append([tier, tests, *stats(group)])
    issues = wb.create_sheet("Execution Errors")
    issues.append(["Task", "Run", "Impl LLM", "Test LLM", "Status", "Error Detail", "Evidence Folder"])
    for r in records:
        if r["status"] not in GOOD_EXECUTIONS:
            issues.append([r["task"], r["run"], r["impl_llm"], r["test_llm"],
                           r["status"], r["error_detail"][:32000], r["evidence"]])
    for sheet in wb:
        sheet.freeze_panes = "A2"
        sheet.auto_filter.ref = sheet.dimensions
        for cell in sheet[1]:
            cell.font = Font(bold=True)
        for column in sheet.iter_cols():
            width = max(len((str(cell.value) if cell.value is not None else "").split("\n")[0]) for cell in column)
            sheet.column_dimensions[get_column_letter(column[0].column)].width = min(max(width + 2, 12), 50)
        for row in sheet.iter_rows(min_row=2):
            for cell in row:
                if isinstance(cell.value, float):
                    cell.number_format = "0.00"
    path = out / "coverage_matrix.xlsx"
    tmp = out / "coverage_matrix.tmp.xlsx"
    wb.save(tmp)
    os.replace(tmp, path)
    return path


def number_list(text, maximum):
    try:
        numbers = set()
        for part in text.split(","):
            if "-" in part:
                a, b = map(int, part.split("-", 1))
                numbers.update(range(a, b + 1))
            else:
                numbers.add(int(part))
        if not numbers or any(n < 1 or n > maximum for n in numbers):
            raise ValueError
        return sorted(numbers)
    except ValueError:
        raise argparse.ArgumentTypeError(f"Use numbers/ranges from 1 to {maximum}, e.g. 1,2,4-6")


def main():
    global OWNED_LOCK
    import threading
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--base-dir", type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument("--output-dir", type=Path, help="Default: BASE_DIR/coverage_results")
    parser.add_argument("--tasks", type=lambda x: number_list(x, 9), default=list(range(1, 10)))
    parser.add_argument("--runs", type=lambda x: number_list(x, 10), default=list(range(1, 11)))
    parser.add_argument("--implementations", nargs="+", choices=LLMS, default=list(LLMS))
    parser.add_argument("--test-sources", nargs="+", choices=LLMS, default=list(LLMS))
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--timeout", type=float, default=120)
    parser.add_argument("--fresh", action="store_true")
    parser.add_argument("--retry-errors", action="store_true")
    parser.add_argument("--retry-checkpoint-errors", action="store_true",
                        help="Retry saved progress.json permission failures; reuse other unchanged results.")
    args = parser.parse_args()
    if args.workers < 1 or args.timeout <= 0:
        parser.error("--workers and --timeout must be positive")
    base = args.base_dir.expanduser().resolve()
    if any(not (base / folder).is_dir() for folder in ["src", "results", "generated_tests"]):
        parser.error(f"{base} must contain src, results and generated_tests. Use --base-dir if needed.")
    try:
        dependencies = {name: importlib.metadata.version(name) for name in ["coverage", "openpyxl"]}
        if dependencies["coverage"].split(".")[0] != "7":
            raise RuntimeError("This script requires coverage.py 7.x.")
    except (importlib.metadata.PackageNotFoundError, RuntimeError) as exc:
        parser.exit(2, f"{exc}\nInstall dependencies: python -m pip install \"coverage>=7.6,<8\" openpyxl\n")
    out = (args.output_dir or base / "coverage_results").expanduser().resolve()
    out.mkdir(parents=True, exist_ok=True)
    lock_path = out / "RUNNING.lock"
    try:
        lock_file = os.open(lock_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        owner = f"PID {os.getpid()}\nStarted {stamp()}\nToken {uuid.uuid4().hex}\n"
        os.write(lock_file, owner.encode())
        os.close(lock_file)
        OWNED_LOCK = (lock_path, owner)
    except FileExistsError:
        parser.exit(2, f"Another run may be using {out}. If it has stopped, delete RUNNING.lock and retry.\n")
    script = Path(__file__).resolve()
    script_hash = hashlib.sha256(script.read_bytes()).hexdigest()
    signature = {"version": VERSION, "script_sha256": script_hash, "python": sys.version,
                 "dependencies": dependencies, "timeout": args.timeout}
    file_cache = {}

    def file_signature(path):
        if path not in file_cache:
            file_cache[path] = hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else "MISSING"
        return file_cache[path]

    jobs = []
    for task in args.tasks:
        for run in args.runs:
            for impl in dict.fromkeys(args.implementations):
                for tests in dict.fromkeys(args.test_sources):
                    impl_path = paths_for(base, task, run, impl, False)
                    test_path = paths_for(base, task, run, tests, True)
                    case_signature = {"task": task,
                        "impl_sha256": file_signature(impl_path), "test_sha256": file_signature(test_path),
                        "impl_path": str(impl_path), "test_path": str(test_path)}
                    def case_fingerprint(settings):
                        return hashlib.sha256(json.dumps({**settings, **case_signature}, sort_keys=True).encode()).hexdigest()
                    fingerprint = case_fingerprint(signature)
                    compatible = [case_fingerprint({**signature, "version": version, "script_sha256": digest})
                                  for version, digest in COMPATIBLE_SIGNATURES]
                    jobs.append({"key": f"task_{task}_run_{run:02d}_impl_{impl}_tests_{tests}",
                                 "task": task, "task_name": TASK_FOLDERS[task], "complexity": COMPLEXITY[task],
                                 "run": run, "impl_llm": impl, "test_llm": tests,
                                 "impl_path": impl_path, "test_path": test_path, "fingerprint": fingerprint,
                                 "compatible_fingerprints": compatible})
    stop_event = threading.Event()
    config = {"out": out, "script": script, "timeout": args.timeout, "fresh": args.fresh,
              "retry_errors": args.retry_errors, "stop_event": stop_event,
              "retry_checkpoint_errors": args.retry_checkpoint_errors}
    atomic_json(out / "run_info.json", {**signature, "started_utc": stamp(), "platform": platform.platform(),
        "base_dir": str(base), "workers": args.workers, "selected_combinations": len(jobs),
        "cache_compatible_script_signatures": [{"version": v, "script_sha256": h} for v, h in COMPATIBLE_SIGNATURES],
        "complexity": COMPLEXITY, "averaging_policy": "Completed nonempty suites only. Failing tests included. Import/load/fixture errors, empty suites, timeouts and unavailable coverage excluded.",
        "coverage_policy": "Statement coverage of the selected implementation only, including import/definition lines. Measurement ends when unittest returns; no interpreter-shutdown/background-timer waiting.",
        "counting_policy": "Disjoint completed test-method outcomes. Failed subtests mark the parent method failed/errored once. Expected failures and unexpected successes are retained in per-case JSON."})
    children = set()
    lock = threading.Lock()
    results = []
    interrupted = False
    started = time.perf_counter()
    print(f"Measuring {len(jobs):,} combinations with {args.workers} workers; {args.timeout:g}s timeout.", flush=True)
    print(f"Output folder: {out}\nUnchanged saved combinations resume automatically.", flush=True)
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=args.workers)
    futures = []
    try:
        futures = [executor.submit(measure_job, job, config, children, lock) for job in jobs]
        with (out / "measurements.jsonl").open("w", encoding="utf-8") as log:
            for future in concurrent.futures.as_completed(futures):
                record = future.result()
                results.append(record)
                log.write(json.dumps(record, ensure_ascii=False) + "\n")
                log.flush()
                n = len(results)
                if n % 25 == 0 or n == len(jobs):
                    print(f"[{n:>4}/{len(jobs)}] {record['key']}: {record['status']} (elapsed {time.perf_counter()-started:.0f}s)", flush=True)
    except KeyboardInterrupt:
        interrupted = True
        stop_event.set()
        print("\nStopping workers. Saved combinations will resume next time.", flush=True)
        for future in futures:
            future.cancel()
        with lock:
            for process in list(children):
                stop_process(process)
    finally:
        executor.shutdown(wait=True, cancel_futures=True)
    if interrupted:
        # Include completed/in-flight records that had not yet reached as_completed.
        known = {r["key"] for r in results}
        for future in futures:
            if not future.cancelled() and future.done() and future.exception() is None:
                record = future.result()
                if record["key"] not in known:
                    results.append(record)
                    known.add(record["key"])
        with (out / "measurements.jsonl").open("w", encoding="utf-8") as log:
            for record in results:
                log.write(json.dumps(record, ensure_ascii=False) + "\n")
    try:
        workbook_path = export_results(results, out)
        print(f"\nSaved {len(results):,} records: {workbook_path}", flush=True)
    except PermissionError:
        print("\nExcel output is open or locked. Close Excel and rerun this command; saved measurements will be reused.", file=sys.stderr)
        return 2
    finally:
        release_run_lock()
    counts = collections.Counter(r["status"] for r in results)
    print("Status totals: " + ", ".join(f"{key}={value}" for key, value in sorted(counts.items())))
    print(f"Included in averages: {sum(r['eligible'] for r in results):,}/{len(results):,}")
    return 130 if interrupted else 0


if __name__ == "__main__":
    if sys.argv[1:] == ["--_worker"]:
        case_child()
    else:
        try:
            raise SystemExit(main())
        finally:
            release_run_lock()
