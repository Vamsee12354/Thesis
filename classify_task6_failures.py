import csv
import re
from collections import Counter
from pathlib import Path

BASE_DIR = Path(r"C:\Users\kalup\Desktop\Thesis")
INPUT_FILE = BASE_DIR / "automation_output" / "task_6_failed_tests.csv"
OUTPUT_DIR = BASE_DIR / "analysis_results" / "task_6_triage"

STATEMENTS = {
    "test_suite_syntax_error": (
        "Test Defect — Syntax Error: The generated test suite contains invalid Python syntax and cannot be imported or executed. Because the test module fails before implementation behavior can be evaluated, the fault lies in the test suite."
    ),
    "implementation_none_runtime_error": (
        "Implementation Defect — Runtime Error: The specification requires missing or invalid password input to be handled safely. However, the implementation calls a string operation on None, raising a runtime error instead of returning the required validation result."
    ),
    "password_length_validation_mismatch": (
        "Password Length Validation Mismatch: The failure concerns the required password length range of 12 to 72 characters. Review the password input and the expected-versus-actual result to determine whether the implementation applies the boundary rule incorrectly or the test expects the wrong result."
    ),
    "special_or_number_validation_mismatch": (
        "Special-or-Number Validation Mismatch: The failure concerns the requirement that a password contain at least one digit or permitted punctuation character. Review the password input and the expected-versus-actual error list to determine fault ownership."
    ),
    "lowercase_validation_mismatch": (
        "Lowercase Validation Mismatch: The failure concerns the requirement that a password contain at least one lowercase letter. Review the password input and the expected-versus-actual error list to determine fault ownership."
    ),
    "uppercase_validation_mismatch": (
        "Uppercase Validation Mismatch: The failure concerns the requirement that a password contain at least one uppercase letter. Review the password input and the expected-versus-actual error list to determine fault ownership."
    ),
    "missing_password_handling_mismatch": (
        "Missing Password Handling Mismatch: The failure concerns the required handling of an empty or missing password. Verify whether the implementation returns the exact required missing-password result and whether the test asserts the correct output type and message."
    ),
    "multiple_password_requirements_mismatch": (
        "Multiple Password Requirements Mismatch: The password violates more than one rule. Inspect the exact input, the required set and order of messages, and the actual output before assigning fault ownership."
    ),
    "unclassified": (
        "Unclassified Failure: The failure cannot be classified reliably from the available test name and traceback. Inspect the test input, expected output, actual output, and implementation behavior."
    ),
}


def normalise(value):
    return str(value or "").lower().replace("-", "_").replace(" ", "_")


def read_text(path_text):
    if not path_text:
        return ""
    try:
        return Path(path_text).read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def assertion_evidence(log_text, test_name):
    if not log_text:
        return "No log text available."

    short_name = str(test_name).split(" (")[0]
    blocks = re.split(r"\n={20,}\n", log_text)

    for block in blocks:
        if short_name in block and any(word in block for word in ("AssertionError", "Error", "SyntaxError")):
            lines = [
                line.strip()
                for line in block.splitlines()
                if any(word in line for word in (
                    "AssertionError", "AttributeError", "TypeError", "SyntaxError",
                    "ImportError", "NameError", "ModuleNotFoundError"
                ))
            ]
            if lines:
                return " | ".join(lines[-2:])[:1200]

    lines = [
        line.strip()
        for line in log_text.splitlines()
        if any(word in line for word in (
            "AssertionError", "AttributeError", "TypeError", "SyntaxError",
            "ImportError", "NameError", "ModuleNotFoundError"
        ))
    ]
    return " | ".join(lines[-2:])[:1200] if lines else "No traceback line extracted."


def classify(test_name, result_type, log_text):
    name = normalise(test_name)
    log = log_text.lower()

    if "test_module_setup/import" in name or "syntaxerror" in log:
        return "test_suite_syntax_error", "Test suite", "High", "No"

    if result_type in {"error", "execution_error"} and any(
        phrase in log
        for phrase in (
            "nonetype",
            "attributeerror",
            "object_of_type_'nonetype'",
            "object of type 'nonetype'",
        )
    ):
        return "implementation_none_runtime_error", "Implementation", "High", "No"

    if any(term in name for term in ("multiple", "all_requirements", "only_special", "only_symbols")):
        return "multiple_password_requirements_mismatch", "Uncertain", "Low", "Yes"

    if any(term in name for term in ("too_long", "too_short", "max_length", "boundary_length", "boundary", "length_")):
        return "password_length_validation_mismatch", "Uncertain", "Medium", "No - spot-check only"

    if any(term in name for term in ("special", "symbol", "number", "digit")):
        return "special_or_number_validation_mismatch", "Uncertain", "Medium", "No - spot-check only"

    if "lowercase" in name or "lower_upper" in name:
        return "lowercase_validation_mismatch", "Uncertain", "Medium", "No - spot-check only"

    if "uppercase" in name:
        return "uppercase_validation_mismatch", "Uncertain", "Medium", "No - spot-check only"

    if any(term in name for term in ("empty_password", "missing_password", "no_password", "password_none", "none_password")):
        return "missing_password_handling_mismatch", "Uncertain", "Medium", "No - spot-check only"

    return "unclassified", "Uncertain", "Low", "Yes"


def write_csv(path, rows, fieldnames):
    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def main():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"Input CSV not found:\n{INPUT_FILE}\n"
            "Update INPUT_FILE at the top of this script if your file was moved."
        )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    with INPUT_FILE.open(newline="", encoding="utf-8-sig") as file:
        source_rows = list(csv.DictReader(file))

    classified = []
    for source in source_rows:
        log_text = read_text(source.get("log_file", ""))
        category, owner, confidence, review_status = classify(
            source.get("test_name", ""),
            source.get("result_type", ""),
            log_text,
        )

        row = dict(source)
        row["provisional_fault_owner"] = owner
        row["provisional_error_category"] = category
        row["provisional_classification"] = STATEMENTS[category]
        row["confidence"] = confidence
        row["review_status"] = review_status
        row["traceback_evidence"] = assertion_evidence(log_text, source.get("test_name", ""))
        row["same_pattern_cross_implementations"] = ""
        row["automation_note"] = (
            "Rule-based first-pass classification using test name, result type, and traceback evidence. "
            "Low-confidence records require manual review; medium-confidence records require category-level spot-checking."
        )
        classified.append(row)

    pattern_counts = Counter(
        (
            row.get("run", ""),
            row.get("test_source", ""),
            row.get("test_name", ""),
            row["provisional_error_category"],
        )
        for row in classified
    )

    for row in classified:
        pattern_key = (
            row.get("run", ""),
            row.get("test_source", ""),
            row.get("test_name", ""),
            row["provisional_error_category"],
        )
        repeated = pattern_counts[pattern_key]
        row["same_pattern_cross_implementations"] = repeated

        if row["confidence"] == "Medium" and repeated >= 4:
            row["confidence"] = "Medium-High"
            row["automation_note"] += (
                " The same run/test-suite/test-name pattern occurs across four or more implementations."
            )

    if not classified:
        raise ValueError("The input CSV contains no failure rows.")

    fieldnames = list(classified[0].keys())

    classified_file = OUTPUT_DIR / "task_6_failed_tests_classified.csv"
    write_csv(classified_file, classified, fieldnames)

    low_queue = [row for row in classified if row["confidence"] == "Low"]
    low_queue_file = OUTPUT_DIR / "task_6_low_confidence_review_queue.csv"
    write_csv(low_queue_file, low_queue, fieldnames)

    summary_counter = Counter(
        (
            row["provisional_error_category"],
            row["provisional_fault_owner"],
            row["confidence"],
        )
        for row in classified
    )

    summary_file = OUTPUT_DIR / "task_6_triage_summary.csv"
    with summary_file.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([
            "provisional_error_category",
            "provisional_fault_owner",
            "confidence",
            "individual_failure_count",
        ])
        for (category, owner, confidence), count in sorted(summary_counter.items()):
            writer.writerow([category, owner, confidence, count])

    confidence_counts = Counter(row["confidence"] for row in classified)
    print(f"Input: {INPUT_FILE}")
    print(f"Classified individual failures: {len(classified)}")
    print(f"High confidence: {confidence_counts['High']}")
    print(f"Medium confidence: {confidence_counts['Medium'] + confidence_counts['Medium-High']}")
    print(f"Low confidence / manual review: {confidence_counts['Low']}")
    print(f"Created: {classified_file}")
    print(f"Created: {low_queue_file}")
    print(f"Created: {summary_file}")


if __name__ == "__main__":
    main()
