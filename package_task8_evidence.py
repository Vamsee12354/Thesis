from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

BASE_DIR = Path(r"C:\Users\kalup\Desktop\Thesis")
TASK_NUMBER = 8
MANUAL_TASK_FOLDER = "task8_slugify"
SOURCES = ("deepseek", "gemma", "mistral", "openai", "amazon")
RUNS = range(1, 11)

OUTPUT_DIR = BASE_DIR / "automation_output"
ZIP_PATH = OUTPUT_DIR / f"task_{TASK_NUMBER}_evidence.zip"


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    files = []
    missing = []

    for run in RUNS:
        for source in SOURCES:
            files.append(
                BASE_DIR / "generated_tests" / source
                / f"task_{TASK_NUMBER}" / f"run_{run:02d}_test.py"
            )
            files.append(
                BASE_DIR / "results" / source
                / f"task_{TASK_NUMBER}" / f"run_{run:02d}.py"
            )

    files.extend([
        BASE_DIR / "src" / MANUAL_TASK_FOLDER / "tests.py",
        BASE_DIR / "src" / MANUAL_TASK_FOLDER / "implementation_manual.py",
        OUTPUT_DIR / f"task_{TASK_NUMBER}_execution_matrix.csv",
        OUTPUT_DIR / f"task_{TASK_NUMBER}_failed_tests.csv",
        OUTPUT_DIR / f"task_{TASK_NUMBER}_review_sheet.csv",
    ])

    log_dir = OUTPUT_DIR / "execution_logs"
    log_pattern = f"task_{TASK_NUMBER}_run_*__tests_*__implementation_*.txt"
    logs = sorted(log_dir.glob(log_pattern)) if log_dir.exists() else []
    files.extend(logs)

    with ZipFile(ZIP_PATH, "w", compression=ZIP_DEFLATED) as archive:
        for path in files:
            if path.is_file():
                archive.write(path, arcname=path.relative_to(BASE_DIR).as_posix())
            else:
                missing.append(path)

        report = [
            f"Task: {TASK_NUMBER}",
            f"Runs requested: {list(RUNS)}",
            f"Sources: {', '.join(SOURCES)} plus manual baseline",
            f"Task-specific logs included: {len(logs)}",
            "",
            "Missing files:",
        ]
        report.extend(str(path.relative_to(BASE_DIR)) for path in missing)
        if not missing:
            report.append("None")
        archive.writestr("MANIFEST.txt", "\n".join(report) + "\n")

    print(f"Created: {ZIP_PATH}")
    print(f"Task-specific logs: {len(logs)}")
    print(f"Missing expected files: {len(missing)}")
    if missing:
        for path in missing:
            print(f"MISSING: {path}")
    print(f"ZIP size: {ZIP_PATH.stat().st_size:,} bytes")


if __name__ == "__main__":
    main()
