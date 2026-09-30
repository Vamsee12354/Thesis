"""
Exports every Task 6 implementation and test-suite source file, run by run,
into Word (.docx) documents, then converts each one to PDF.

Requires:
    pip install python-docx
    pip install docx2pdf      (Windows/Mac only, needs Microsoft Word installed)

If Word is not installed, this script will still produce the .docx files and
tell you how to convert them with LibreOffice instead.

For each run 1-10, creates one docx (and matching pdf) containing:
  - every implementation_manual.py used in that run (Manual, Deepseek, Gemma,
    Mistral, OpenAI, Amazon), and
  - every selected_test.py (test suite) used in that run,
grouped by test-suite / implementation pairing, exactly as executed.

No mixing between runs: each document contains only that run's own files.
No duplicate pairings.
"""

import re
import shutil
import subprocess
from pathlib import Path

try:
    from docx import Document
    from docx.shared import Pt, RGBColor
    from docx.enum.text import WD_ALIGN_PARAGRAPH
except ImportError:
    raise SystemExit(
        "python-docx is not installed. Run this first:\n\n"
        "    pip install python-docx\n"
    )

BASE_DIR = Path(r"C:\Users\kalup\Desktop\Thesis")

# Only ONE search root is used. Searching multiple nested roots (e.g. a
# folder and its own parent folder) causes every match to be found once per
# root, which caused the earlier triplicated output.
SEARCH_ROOT = BASE_DIR / "automation_output" / "_temporary_execution"
FALLBACK_ROOT = BASE_DIR  # used only if SEARCH_ROOT does not exist

OUTPUT_DIR = BASE_DIR / "task_6_docx_export"

RUN_PATTERN = re.compile(r"^task_6_run_(\d{1,2})__tests_([^_]+)__implementation_(.+)$", re.I)


def find_run_folders():
    """Locate every task_6_run_XX__tests_YYY__implementation_ZZZ folder exactly once."""
    root = SEARCH_ROOT if SEARCH_ROOT.exists() else FALLBACK_ROOT
    if not root.exists():
        return {}, root

    unique_paths = {}
    for path in root.rglob("task_6_run_*__tests_*__implementation_*"):
        if not path.is_dir():
            continue
        match = RUN_PATTERN.match(path.name)
        if not match:
            continue
        unique_paths[path.resolve()] = match

    folders = {}
    for resolved_path, match in unique_paths.items():
        run = int(match.group(1))
        test_suite = match.group(2)
        implementation = match.group(3)
        folders.setdefault(run, []).append((test_suite, implementation, resolved_path))

    return folders, root


def add_code_block(document, code_text):
    paragraph = document.add_paragraph()
    run = paragraph.add_run(code_text if code_text.strip() else "[File not found or empty]")
    run.font.name = "Consolas"
    run.font.size = Pt(9)
    run.font.color.rgb = RGBColor(0x20, 0x20, 0x20)
    paragraph.paragraph_format.space_after = Pt(12)


def add_heading(document, text, level=1):
    heading = document.add_heading(text, level=level)
    heading.alignment = WD_ALIGN_PARAGRAPH.LEFT
    return heading


def add_subheading(document, text):
    paragraph = document.add_paragraph()
    run = paragraph.add_run(text)
    run.bold = True
    run.font.size = Pt(12)
    paragraph.paragraph_format.space_before = Pt(10)
    paragraph.paragraph_format.space_after = Pt(4)


def read_source(folder, filename):
    file_path = folder / filename
    if not file_path.exists():
        return None
    try:
        return file_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None


def build_run_document(run_number, entries):
    document = Document()
    add_heading(document, f"Task 6 \u2014 Run {run_number}", level=0)
    document.add_paragraph(
        f"This document contains only Run {run_number}'s own implementations and test "
        "suites, exactly as executed. No files from any other run are included."
    )

    seen_pairs = set()
    entries_unique = []
    for test_suite, implementation, folder in entries:
        pair_key = (test_suite.lower(), implementation.lower())
        if pair_key in seen_pairs:
            continue
        seen_pairs.add(pair_key)
        entries_unique.append((test_suite, implementation, folder))

    entries_sorted = sorted(entries_unique, key=lambda item: (item[0].lower(), item[1].lower()))

    for test_suite, implementation, folder in entries_sorted:
        add_heading(document, f"Test suite: {test_suite}  \u2192  Implementation: {implementation}", level=1)

        add_subheading(document, "implementation_manual.py")
        impl_text = read_source(folder, "implementation_manual.py")
        add_code_block(document, impl_text)

        add_subheading(document, "selected_test.py")
        test_text = read_source(folder, "selected_test.py")
        add_code_block(document, test_text)

        document.add_page_break()

    return document, len(entries_sorted)


# ---------------------------------------------------------------------------
# PDF conversion
# ---------------------------------------------------------------------------

def convert_with_docx2pdf(docx_paths):
    """Try converting via docx2pdf (uses Microsoft Word on Windows/Mac)."""
    try:
        from docx2pdf import convert
    except ImportError:
        return False, "docx2pdf is not installed (pip install docx2pdf)."

    try:
        for docx_path in docx_paths:
            convert(str(docx_path))
        return True, None
    except Exception as error:
        return False, f"docx2pdf failed: {error}"


def convert_with_libreoffice(docx_paths, output_dir):
    """Fallback: convert via LibreOffice headless mode, if installed."""
    soffice = shutil.which("soffice") or shutil.which("soffice.exe")
    if not soffice:
        return False, "LibreOffice ('soffice') was not found on PATH."

    try:
        for docx_path in docx_paths:
            subprocess.run(
                [soffice, "--headless", "--convert-to", "pdf", "--outdir", str(output_dir), str(docx_path)],
                check=True,
                capture_output=True,
            )
        return True, None
    except subprocess.CalledProcessError as error:
        return False, f"LibreOffice conversion failed: {error}"


def convert_all_to_pdf(docx_paths, output_dir):
    print("\nConverting to PDF...")
    ok, error = convert_with_docx2pdf(docx_paths)
    if ok:
        print("Converted using Microsoft Word (docx2pdf).")
        return True

    print(f"docx2pdf unavailable or failed: {error}")
    print("Trying LibreOffice instead...")
    ok, error = convert_with_libreoffice(docx_paths, output_dir)
    if ok:
        print("Converted using LibreOffice.")
        return True

    print(f"LibreOffice conversion also unavailable: {error}")
    print(
        "\nCould not convert automatically. The .docx files were still created "
        f"in:\n{output_dir}\n\n"
        "To convert manually, do ONE of the following:\n"
        "  1. Install Microsoft Word, then run:\n"
        "         pip install docx2pdf\n"
        "         python export_task6_runs_to_docx.py\n"
        "  2. Install LibreOffice (free), make sure 'soffice' is on your PATH, "
        "then rerun this script.\n"
        "  3. Open each .docx in Word manually and use File > Save As > PDF."
    )
    return False


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    run_folders, root_used = find_run_folders()

    if not run_folders:
        raise SystemExit(
            f"No task_6_run_XX__tests_YYY__implementation_ZZZ folders were found under:\n{root_used}\n\n"
            "Update SEARCH_ROOT at the top of this script if your files are elsewhere."
        )

    print(f"Search root: {root_used}\n")

    created_docx = []
    for run_number in sorted(run_folders):
        entries = run_folders[run_number]
        document, count = build_run_document(run_number, entries)
        output_path = OUTPUT_DIR / f"task_6_run_{run_number:02d}.docx"
        document.save(output_path)
        created_docx.append(output_path)
        print(f"Run {run_number:>2}: {count} unique test-suite/implementation pairing(s) -> {output_path}")

    missing_runs = [r for r in range(1, 11) if r not in run_folders]
    if missing_runs:
        print(f"\nNo folders found for run(s): {', '.join(str(r) for r in missing_runs)}")
        print("Check SEARCH_ROOT or the folder naming pattern if these runs should exist.")

    convert_all_to_pdf(created_docx, OUTPUT_DIR)


if __name__ == "__main__":
    main()
