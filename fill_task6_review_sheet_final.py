import ast
import csv
import re
from collections import defaultdict
from pathlib import Path

BASE_DIR = Path(r"C:\Users\kalup\Desktop\Thesis")
TRIAGE_DIR = BASE_DIR / "analysis_results" / "task_6_triage"

REVIEW_CANDIDATES = [
    BASE_DIR / "automation_output" / "task_6_review_sheet.csv",
    BASE_DIR / "task_6_review_sheet.csv",
    TRIAGE_DIR / "task_6_review_sheet.csv",
]
CLASSIFIED_CANDIDATES = [
    TRIAGE_DIR / "task_6_failed_tests_classified.csv",
    BASE_DIR / "automation_output" / "task_6_failed_tests_classified.csv",
    BASE_DIR / "task_6_failed_tests_classified.csv",
]
OUTPUT_FILE = TRIAGE_DIR / "task_6_review_sheet_final.csv"

RULE_NAME = {
    "Length must be between 12 and 72 characters": "the length requirement (12 to 72 characters)",
    "Password must contain a lowercase letter": "the lowercase-letter requirement",
    "Password must contain an uppercase letter": "the uppercase-letter requirement",
    "Password must contain a special character or a number": "the special-character-or-number requirement",
    "Please fill the password": "the missing-password requirement",
}


def find_file(candidates, description):
    for path in candidates:
        if path.exists():
            return path
    checked = "\n".join(f"- {path}" for path in candidates)
    raise FileNotFoundError(f"Could not find {description}. Checked:\n{checked}")


def key(row):
    return (
        str(row.get("Run", row.get("run", ""))).strip(),
        str(row.get("Test LLM", row.get("test_source", ""))).strip().lower(),
        str(row.get("Implementation LLM", row.get("implementation_source", ""))).strip().lower(),
    )


# ---------------------------------------------------------------------------
# Log parsing
# ---------------------------------------------------------------------------

def read_log(log_path_text):
    if not log_path_text:
        return ""
    path = Path(log_path_text)
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def find_block(log_text, test_name):
    if not log_text:
        return ""
    headers = list(re.finditer(r"^(FAIL|ERROR): (.+)$", log_text, re.M))
    for idx, match in enumerate(headers):
        if match.group(2).strip() == test_name.strip():
            start = match.end()
            end = headers[idx + 1].start() if idx + 1 < len(headers) else len(log_text)
            return log_text[start:end]
    return ""


def try_literal(text):
    text = text.strip()
    try:
        return ast.literal_eval(text)
    except Exception:
        return None


def extract_diff_lists(block):
    minus_lines, plus_lines = [], []
    started = False
    for line in block.splitlines():
        if line.startswith("- "):
            started = True
            minus_lines.append(line[2:])
        elif line.startswith("+ "):
            started = True
            plus_lines.append(line[2:])
        elif line.startswith("? "):
            continue
        elif started and not line.strip():
            break
    actual = try_literal("\n".join(minus_lines)) if minus_lines else None
    expected = try_literal("\n".join(plus_lines)) if plus_lines else None
    return actual, expected


def extract_assertion(block):
    m = re.search(r"AssertionError:\s*(?:Lists differ:\s*)?(.*)$", block, re.M)
    if not m:
        return None, None
    one_liner = m.group(1)
    single = re.match(r"^(.*?)\s!=\s(.*)$", one_liner)
    has_diff_block = "\n- " in block or block.strip().startswith("- ")
    if single and not has_diff_block:
        actual = try_literal(single.group(1))
        expected = try_literal(single.group(2))
        if actual is not None or expected is not None:
            return actual, expected
    return extract_diff_lists(block)


def extract_exception(block):
    matches = list(re.finditer(r"^(\w+(?:Error|Exception)):\s*(.*)$", block, re.M))
    if not matches:
        return None, None
    last = matches[-1]
    return last.group(1), last.group(2)


def as_rule_list(names):
    if not names:
        return ""
    labels = [RULE_NAME.get(n, n) for n in names]
    if len(labels) == 1:
        return labels[0]
    return ", ".join(labels[:-1]) + " and " + labels[-1]


def humanize_exc(exc_type):
    return re.sub(r"(?<!^)(?=[A-Z])", " ", exc_type).strip()


# ---------------------------------------------------------------------------
# Per-test decision. Returns:
#   fault_owner   -> "Test Error" | "Implementation Defect" | "Both Faulty"
#                    | "Test Suite Defect" | "Needs Check"
#   error_kind    -> "Assertion Error" | "Type Error" | "Syntax Error" | etc.
#   body          -> the explanatory sentence(s), no heading, no counts.
# ---------------------------------------------------------------------------

def decide(row):
    log_text = read_log(row.get("log_file", ""))
    test_name = str(row.get("test_name", ""))
    block = find_block(log_text, test_name)

    if not block:
        return ("Needs Check", "Missing Evidence",
                "The execution log for this test could not be located or matched. Inspect the "
                "original log file to determine the exact actual and expected values.")

    if "SyntaxError" in block and "selected_test.py" in block:
        return ("Test Suite Defect", "Syntax Error",
                "The generated test module contains invalid Python syntax and cannot be imported. "
                "Execution stops before any implementation behaviour can be evaluated.")

    if "ImportError" in block and "implementation_manual" in block and "cannot import name" in block:
        _, msg = extract_exception(block)
        return ("Implementation Defect", "Import Error",
                f"{(msg or 'The implementation does not expose the required IsValidPassword function').strip()}. "
                "The task specification requires the public function IsValidPassword to be importable and callable.")

    if "AssertionError" not in block:
        exc_type, msg = extract_exception(block)
        if exc_type:
            return ("Implementation Defect", humanize_exc(exc_type),
                    f"The implementation raises a {humanize_exc(exc_type)} "
                    f"({(msg or 'no message captured').strip()}) instead of returning a validation result. "
                    "The specification requires all inputs, including missing or unusual passwords, to be "
                    "handled safely and return a validation result rather than raise an exception.")
        return ("Needs Check", "Missing Evidence",
                "The log does not contain a recognisable AssertionError or exception line for this test.")

    actual, expected = extract_assertion(block)
    if actual is None or expected is None:
        return ("Needs Check", "Missing Evidence",
                "The actual and expected values for this assertion could not be reliably extracted "
                "from the log text.")

    # One side is a bare string, the other a one-item list with the same message.
    if isinstance(actual, str) and isinstance(expected, list) and len(expected) == 1 and expected[0] == actual:
        return ("Implementation Defect", "Assertion Error",
                f"The implementation returns the string \"{actual}\" instead of the required list "
                f"{expected!r}. The Task 6 specification's own example shows this case returning a list, "
                "so the implementation's return type is incorrect.")
    if isinstance(expected, str) and isinstance(actual, list) and len(actual) == 1 and actual[0] == expected:
        return ("Test Error", "Assertion Error",
                f"The test expects the string \"{expected}\", but the specification's own example shows "
                f"this case returning the list {actual!r}. The implementation is correct; the test's "
                "expected value does not match the documented return type.")

    if not isinstance(actual, list) or not isinstance(expected, list):
        return ("Needs Check", "Assertion Error",
                f"The implementation returns {actual!r} while the test expects {expected!r}. One side "
                "treats this password as valid and the other as invalid; the exact password is needed "
                "to confirm which side is correct.")

    missing = [e for e in actual if e not in expected]
    extra = [e for e in expected if e not in actual]

    if not missing and not extra:
        return ("Needs Check", "Missing Evidence",
                "The actual and expected lists extracted from the log are identical, which is "
                "inconsistent with a recorded failure. Re-run this test to confirm the outcome.")

    if missing and not extra:
        return ("Test Error", "Assertion Error",
                f"The implementation returns {actual!r}, correctly including {as_rule_list(missing)} in "
                f"addition to the rule(s) already in the test's expected list. However, the test expects "
                f"only {expected!r}, so its expected value is incomplete and omits {as_rule_list(missing)}.")

    if extra and not missing:
        return ("Implementation Defect", "Assertion Error",
                f"The test expects {expected!r}, but the implementation returns only {actual!r}, failing "
                f"to detect {as_rule_list(extra)} for this password. The implementation does not correctly "
                f"check {as_rule_list(extra)} for this input.")

    return ("Both Faulty", "Assertion Error",
            f"The implementation returns {actual!r} while the test expects {expected!r}. The implementation "
            f"incorrectly reports {as_rule_list(missing)}, and the test incorrectly expects "
            f"{as_rule_list(extra)}. Both the test and the implementation require correction.")


def notes_for(rows, complete):
    if complete:
        return "All tests passed\n\nNo failed test was recorded for this test-suite and implementation pairing."
    if not rows:
        return ("No matching individual failure record\n\nNeeds Check: No individual failed-test record "
                "matched this Run, Test LLM, and Implementation LLM combination.")

    grouped = defaultdict(list)
    for row in rows:
        owner, kind, body = decide(row)
        grouped[(owner, kind)].append(body)

    sections = []
    for (owner, kind), bodies in grouped.items():
        unique_bodies = []
        for b in bodies:
            if b not in unique_bodies:
                unique_bodies.append(b)
        count = len(unique_bodies)
        plural = "s" if count > 1 else ""
        heading = f"{owner}: {count} {kind}{plural}:" if count > 1 else f"{owner}: {kind}:"
        if count == 1:
            sections.append(f"{heading} {unique_bodies[0]}")
        else:
            numbered = "\n\n".join(f"{i}. {b}" for i, b in enumerate(unique_bodies, 1))
            sections.append(f"{heading}\n\n{numbered}")

    return "\n\n---\n\n".join(sections)


def decide_fault_classification(rows, complete):
    if complete:
        return "No failure"
    if not rows:
        return "Needs Check"
    owners = {decide(row)[0] for row in rows}
    return next(iter(owners)) if len(owners) == 1 else "Mixed — see Notes"


def need_to_check_text(rows, complete):
    if complete:
        return "No"
    if not rows:
        return "Yes — no matching individual failure record"
    flagged = [row for row in rows if decide(row)[0] == "Needs Check"]
    if not flagged:
        return "No"
    return f"Yes — {len(flagged)} of {len(rows)} individual failure(s) require review"


def output_field_order(original_fields):
    fields = [f for f in original_fields if f not in {"Fault classification", "Need to check?"}]
    if "Notes" not in fields:
        fields.append("Notes")
    notes_position = fields.index("Notes") + 1
    fields.insert(notes_position, "Fault classification")
    fields.insert(notes_position + 1, "Need to check?")
    return fields


def main():
    review_file = find_file(REVIEW_CANDIDATES, "Task 6 review sheet")
    classified_file = find_file(CLASSIFIED_CANDIDATES, "classified Task 6 failures")
    TRIAGE_DIR.mkdir(parents=True, exist_ok=True)

    with review_file.open(newline="", encoding="utf-8-sig") as file:
        review_rows = list(csv.DictReader(file))
        original_fields = list(review_rows[0].keys()) if review_rows else []

    with classified_file.open(newline="", encoding="utf-8-sig") as file:
        classified_rows = list(csv.DictReader(file))

    grouped_failures = defaultdict(list)
    for row in classified_rows:
        grouped_failures[key(row)].append(row)

    explained = passed = unmatched = needs_check_rows = 0

    for row in review_rows:
        if not any(str(value or "").strip() for value in row.values()):
            continue

        complete = str(row.get("Complete?", "")).strip().lower() == "yes"
        failures = grouped_failures.get(key(row), [])

        row["Notes"] = notes_for(failures, complete)
        row["Fault classification"] = decide_fault_classification(failures, complete)
        row["Need to check?"] = need_to_check_text(failures, complete)

        if complete:
            passed += 1
        elif not failures:
            unmatched += 1
        else:
            explained += 1
        if row["Need to check?"].startswith("Yes"):
            needs_check_rows += 1

    fields = output_field_order(original_fields)
    with OUTPUT_FILE.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(review_rows)

    print(f"Review sheet used: {review_file}")
    print(f"Classified failures used: {classified_file}")
    print(f"Rows with detailed explanations: {explained}")
    print(f"All-pass rows: {passed}")
    print(f"Rows requiring manual inspection: {needs_check_rows}")
    print(f"Unmatched rows: {unmatched}")
    print(f"Created: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
