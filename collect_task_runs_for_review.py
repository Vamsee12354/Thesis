import argparse
import csv
import re
import shutil
import zipfile
from pathlib import Path

BASE_DIR = Path(r"C:\Users\kalup\Desktop\Thesis")
OUTPUT_DIR = BASE_DIR / "review_packages"
SKIP_DIRS = {"analysis_results", "review_packages", ".git", "__pycache__", ".venv", "venv", "node_modules"}
SOURCE_SUFFIXES = {".py", ".txt", ".log", ".csv", ".json", ".md", ".pdf", ".docx"}


def normalise(text):
    return str(text).lower().replace("\\", "/")


def task_matches(relative_path, task):
    text = normalise(relative_path)
    patterns = [
        rf"task[_\- ]*0*{task}(?!\d)",
        rf"execution[_\- ]*0*{task}(?!\d)",
        rf"selected[_\- ]*task[_\- ]*0*{task}(?!\d)",
    ]
    return any(re.search(pattern, text) for pattern in patterns)


def run_number(relative_path):
    text = normalise(relative_path)
    matches = re.findall(r"run[_\- ]*0?(10|[1-9])(?!\d)", text)
    return int(matches[-1]) if matches else None


def should_skip(path):
    return any(part.lower() in SKIP_DIRS for part in path.parts)


def copy_file(source, destination_root):
    relative = source.relative_to(BASE_DIR)
    target = destination_root / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)
    return target


def add_if_exists(path, staging_root, manifest, label):
    if path.exists() and path.is_file():
        copy_file(path, staging_root)
        manifest.append({"file": str(path.relative_to(BASE_DIR)), "run": "", "type": label})
        return True
    return False


def make_zip(staging_root, zip_path):
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for file_path in staging_root.rglob("*"):
            if file_path.is_file():
                archive.write(file_path, file_path.relative_to(staging_root))


def main():
    parser = argparse.ArgumentParser(
        description="Collect all source files, logs, and review data for one thesis task into a ZIP package."
    )
    parser.add_argument("--task", type=int, required=True, help="Task number, for example: --task 6")
    args = parser.parse_args()
    task = args.task

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    staging_root = OUTPUT_DIR / f"task_{task}_review_package"
    zip_path = OUTPUT_DIR / f"task_{task}_review_package.zip"

    if staging_root.exists():
        shutil.rmtree(staging_root)
    staging_root.mkdir(parents=True)

    manifest = []
    found_runs = {run: [] for run in range(1, 11)}
    copied_sources = set()

    for source in BASE_DIR.rglob("*"):
        if not source.is_file() or should_skip(source.relative_to(BASE_DIR)):
            continue
        if source.suffix.lower() not in SOURCE_SUFFIXES:
            continue

        relative = source.relative_to(BASE_DIR)
        relative_text = normalise(relative)
        is_task_file = task_matches(relative, task)
        run = run_number(relative)

        is_shared_review_data = (
            is_task_file
            and source.suffix.lower() == ".csv"
            and any(word in relative_text for word in ("failed", "review_sheet", "execution_matrix"))
        )
        is_task_log = is_task_file and source.suffix.lower() in {".txt", ".log"}
        is_task_source = is_task_file and source.suffix.lower() == ".py"
        is_task_spec = is_task_file and source.suffix.lower() in {".md", ".pdf", ".docx", ".txt"}

        if not (is_shared_review_data or is_task_log or is_task_source or is_task_spec):
            continue

        if relative in copied_sources:
            continue
        copied_sources.add(relative)
        copy_file(source, staging_root)

        file_type = "review_data" if is_shared_review_data else "log" if is_task_log else "python_source" if is_task_source else "specification_or_text"
        manifest.append({"file": str(relative), "run": run or "shared", "type": file_type})
        if run in found_runs:
            found_runs[run].append(str(relative))

    important_files = [
        (BASE_DIR / "automation_output" / f"task_{task}_failed_tests.csv", "failed_test_records"),
        (BASE_DIR / "automation_output" / f"task_{task}_review_sheet.csv", "original_review_sheet"),
        (BASE_DIR / "automation_output" / f"task_{task}_execution_matrix.csv", "execution_matrix"),
        (BASE_DIR / "analysis_results" / f"task_{task}_triage" / f"task_{task}_review_sheet_final.csv", "final_review_sheet"),
        (BASE_DIR / "analysis_results" / f"task_{task}_triage" / f"task_{task}_failed_tests_classified.csv", "classified_failures"),
    ]
    for path, label in important_files:
        add_if_exists(path, staging_root, manifest, label)

    manifest_path = staging_root / "MANIFEST.csv"
    with manifest_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["file", "run", "type"])
        writer.writeheader()
        writer.writerows(manifest)

    summary_path = staging_root / "README.txt"
    with summary_path.open("w", encoding="utf-8") as file:
        file.write(f"Task {task} review package\n")
        file.write("This package was collected without mixing runs.\n\n")
        for run in range(1, 11):
            count = len(found_runs[run])
            status = "FOUND" if count else "NOT FOUND"
            file.write(f"Run {run}: {status} ({count} task/run-labelled file(s))\n")
        file.write("\nThe package includes Manual, Deepseek, Gemma, Mistral, OpenAI, and Amazon files whenever their paths or filenames identify the requested task.\n")
        file.write("Check MANIFEST.csv before sharing the ZIP. If a run says NOT FOUND, locate its test/implementation folder and place it under a path containing task_<number> and run_<number>, then rerun this script.\n")

    make_zip(staging_root, zip_path)

    print(f"Created folder: {staging_root}")
    print(f"Created ZIP: {zip_path}")
    for run in range(1, 11):
        print(f"Run {run}: {len(found_runs[run])} task/run-labelled file(s) found")
    print(f"Total copied files: {len(manifest)}")
    print("Open MANIFEST.csv and README.txt in the package to verify coverage before uploading the ZIP.")


if __name__ == "__main__":
    main()
