from __future__ import annotations

import csv
import re
from pathlib import Path

# --- edit these if needed ---
FAILED_CSV = Path(r"C:\Users\kalup\Desktop\Thesis\automation_output\task_5_failed_tests.csv")
OUTPUT_CSV = Path(r"C:\Users\kalup\Desktop\Thesis\automation_output\task_5_failed_tests_with_errors.csv")
# ----------------------------

FAIL_HEADER_RE = re.compile(
    r"^(?:FAIL|ERROR):\s*(.+?)(?:\s+\(.*\))?$"
)
TRACE_END_RE = re.compile(
    r"^(?:AssertionError|TypeError|ValueError|AttributeError|KeyError|"
    r"IndexError|NameError|SyntaxError|ImportError|ModuleNotFoundError|"
    r"RuntimeError|Exception|Error)(?::\s*.*)?$"
)
SUMMARY_RE = re.compile(r"^(?:FAILED|ERROR|OK|Ran \d+ test)")


def short_test_name(full_name: str) -> str:
    """
    'test_x (selected_test.Class.test_x)' -> 'test_x'
    'Test module setup/import' -> same
    """
    full_name = (full_name or "").strip()
    if " (" in full_name:
        return full_name.split(" (", 1)[0].strip()
    return full_name


def extract_error_block(log_text: str, test_name: str) -> str:
    lines = log_text.splitlines()
    target = short_test_name(test_name)

    # Suite-level import/setup crash
    if target.lower() in {
        "test module setup/import",
        "module setup/import",
        "setup/import",
    }:
        for i, line in enumerate(lines):
            if "SyntaxError" in line or "ImportError" in line or "ModuleNotFoundError" in line:
                start = max(0, i - 8)
                end = min(len(lines), i + 3)
                return "\n".join(lines[start:end]).strip()
        # fallback: last non-empty chunk
        tail = [ln for ln in lines[-40:] if ln.strip()]
        return "\n".join(tail[-15:]).strip() if tail else "NO_ERROR_FOUND"

    # Find FAIL:/ERROR: header matching this test
    start_idx = None
    for i, line in enumerate(lines):
        m = FAIL_HEADER_RE.match(line.strip())
        if not m:
            continue
        header_name = short_test_name(m.group(1))
        if header_name == target or target in line or header_name in target:
            start_idx = i
            break

    # Fallback: first line containing the test function name
    if start_idx is None:
        for i, line in enumerate(lines):
            if target in line and ("FAIL" in line or "ERROR" in line or "AssertionError" in line):
                start_idx = i
                break

    if start_idx is None:
        return "NO_ERROR_FOUND"

    # Collect until next FAIL/ERROR header or unittest summary
    block: list[str] = []
    for j in range(start_idx, min(len(lines), start_idx + 80)):
        ln = lines[j]
        if j > start_idx and FAIL_HEADER_RE.match(ln.strip()):
            break
        if j > start_idx and SUMMARY_RE.match(ln.strip()):
            break
        block.append(ln)

    # Prefer the final exception line + a bit of context
    exc_idx = None
    for k in range(len(block) - 1, -1, -1):
        if TRACE_END_RE.match(block[k].strip()) or block[k].strip().startswith(
            ("AssertionError", "TypeError", "SyntaxError", "AttributeError", "ValueError")
        ):
            exc_idx = k
            break

    if exc_idx is not None:
        start = max(0, exc_idx - 6)
        return "\n".join(block[start : exc_idx + 1]).strip()

    # otherwise return trimmed block
    cleaned = [ln for ln in block if ln.strip()]
    return "\n".join(cleaned[:20]).strip() if cleaned else "NO_ERROR_FOUND"


def main() -> None:
    if not FAILED_CSV.exists():
        raise SystemExit(f"Input not found: {FAILED_CSV}")

    with FAILED_CSV.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames or [])
        rows = list(reader)

    if "error_message" not in fieldnames:
        # put error text near the notes columns
        insert_at = len(fieldnames)
        for key in ("manual_notes", "error_category", "failure_cause", "log_file"):
            if key in fieldnames:
                insert_at = fieldnames.index(key) + (0 if key == "log_file" else 1)
                if key == "log_file":
                    insert_at = fieldnames.index(key) + 1
                break
        fieldnames.insert(min(insert_at, len(fieldnames)), "error_message")

    cache: dict[str, str] = {}
    missing_logs = 0
    found = 0

    for row in rows:
        log_path = (row.get("log_file") or "").strip()
        test_name = (row.get("test_name") or "").strip()

        if not log_path:
            row["error_message"] = "NO_LOG_PATH"
            continue

        p = Path(log_path)
        if not p.exists():
            row["error_message"] = f"LOG_NOT_FOUND: {log_path}"
            missing_logs += 1
            continue

        if log_path not in cache:
            try:
                cache[log_path] = p.read_text(encoding="utf-8", errors="replace")
            except Exception as e:
                cache[log_path] = ""
                row["error_message"] = f"LOG_READ_ERROR: {e}"
                continue

        msg = extract_error_block(cache[log_path], test_name)
        row["error_message"] = msg
        if msg not in {"NO_ERROR_FOUND", ""} and not msg.startswith("LOG_"):
            found += 1

    OUTPUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_CSV.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

    print("Done.")
    print(f"Rows:         {len(rows)}")
    print(f"Errors found: {found}")
    print(f"Missing logs: {missing_logs}")
    print(f"Output:       {OUTPUT_CSV}")


if __name__ == "__main__":
    main()