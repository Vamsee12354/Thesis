from pathlib import Path


# ==================================================
# SELECT TASK AND RUN TO DISPLAY
# ==================================================

TASK_NUMBER = "9"
RUN_NUMBER = 10


# ==================================================
# MANUAL TASK FOLDER NAMES
# ==================================================

MANUAL_TASK_FOLDERS = {
    "1": "task1_unique_brands",
    "2": "task2_get_average_price",
    "3": "task3_get_min_attribute",
    "4": "task4_get_reading_duration",
    "5": "task5_validate_contact_form",
    "6": "task6_validate_password",
    "7": "task7_product_list_live_view",
    "8": "task8_slugify",
    "9": "task9_product_cache_get",
}


# ==================================================
# PROJECT SETTINGS
# ==================================================

BASE_DIR = Path(r"C:\Users\kalup\Desktop\Thesis")

LLMS = [
    "deepseek",
    "gemma",
    "mistral",
    "openai",
    "amazon",
]

ALL_SOURCES = LLMS + ["manual"]

MANUAL_TASK_FOLDER = MANUAL_TASK_FOLDERS[TASK_NUMBER]


# ==================================================
# DISPLAY-NAME FUNCTION
# ==================================================

def display_name(source: str) -> str:
    """Convert folder names into readable names."""
    source_names = {
        "deepseek": "DeepSeek",
        "gemma": "Gemma",
        "mistral": "Mistral",
        "openai": "OpenAI",
        "amazon": "Amazon",
        "manual": "Manual",
    }

    return source_names.get(source.lower(), source)


# ==================================================
# PATH FUNCTIONS
# ==================================================

def get_test_file(source: str) -> Path:
    """Return the test file for one LLM/manual source."""
    if source == "manual":
        return (
            BASE_DIR
            / "src"
            / MANUAL_TASK_FOLDER
            / "tests.py"
        )

    return (
        BASE_DIR
        / "generated_tests"
        / source
        / f"task_{TASK_NUMBER}"
        / f"run_{RUN_NUMBER:02d}_test.py"
    )


def get_implementation_file(source: str) -> Path:
    """Return the implementation file for one LLM/manual source."""
    if source == "manual":
        return (
            BASE_DIR
            / "src"
            / MANUAL_TASK_FOLDER
            / "implementation_manual.py"
        )

    return (
        BASE_DIR
        / "results"
        / source
        / f"task_{TASK_NUMBER}"
        / f"run_{RUN_NUMBER:02d}.py"
    )


# ==================================================
# PRINT FILE CONTENT
# ==================================================

def print_code_block(
    title: str,
    source: str,
    file_path: Path,
) -> None:
    """Print one file with clear separators for copying."""
    print("\n" + "=" * 100)
    print(title)
    print("=" * 100)
    print(f"Source: {display_name(source)}")
    print(f"File:   {file_path}")
    print("-" * 100)

    if not file_path.exists():
        print("FILE MISSING")
        print("=" * 100)
        return

    try:
        code = file_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        code = file_path.read_text(encoding="utf-8-sig")
    except OSError as error:
        print(f"COULD NOT READ FILE: {error}")
        print("=" * 100)
        return

    print(code.rstrip())
    print("\n" + "=" * 100)


# ==================================================
# PRINT ONE COMPLETE RUN
# ==================================================

def main() -> None:
    if TASK_NUMBER not in MANUAL_TASK_FOLDERS:
        print("TASK_NUMBER must be between 1 and 9.")
        return

    print("\n" + "#" * 100)
    print("THESIS SOURCE-CODE FETCHER — NO TESTS ARE EXECUTED")
    print("#" * 100)
    print(f"Task: {TASK_NUMBER}")
    print(f"Run:  {RUN_NUMBER:02d}")
    print("Included sources: DeepSeek, Gemma, Mistral, OpenAI, Amazon, Manual")
    print("#" * 100)

    # --------------------------------------------------
    # All tests that belong to this run
    # --------------------------------------------------

    print("\n" + "#" * 100)
    print(f"TEST SUITES — TASK {TASK_NUMBER}, RUN {RUN_NUMBER:02d}")
    print("#" * 100)

    for source in ALL_SOURCES:
        if source == "manual":
            run_label = "Manual baseline"
        else:
            run_label = f"Run {RUN_NUMBER:02d}"

        print_code_block(
            (
                f"TEST SUITE: {display_name(source).upper()} "
                f"| {run_label}"
            ),
            source,
            get_test_file(source),
        )

    # --------------------------------------------------
    # All implementations that belong to this run
    # --------------------------------------------------

    print("\n" + "#" * 100)
    print(f"IMPLEMENTATIONS — TASK {TASK_NUMBER}, RUN {RUN_NUMBER:02d}")
    print("#" * 100)

    for source in ALL_SOURCES:
        if source == "manual":
            run_label = "Manual baseline"
        else:
            run_label = f"Run {RUN_NUMBER:02d}"

        print_code_block(
            (
                f"IMPLEMENTATION: {display_name(source).upper()} "
                f"| {run_label}"
            ),
            source,
            get_implementation_file(source),
        )

    print("\n" + "#" * 100)
    print("END OF RUN SOURCE-CODE BLOCK")
    print("#" * 100 + "\n")


if __name__ == "__main__":
    main()