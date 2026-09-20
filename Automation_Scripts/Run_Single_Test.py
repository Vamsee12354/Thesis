import os
import shutil
import subprocess
import sys


TASK_NUMBER = "6"
# manual, gemma, deepseek, mistral, openai, amazon
TEST_LLM = "deepseek"
# manual, gemma, deepseek, mistral, openai, amazon
IMPLEMENTATION_LLM = "deepseek"
TEST_RUN = 1
IMPLEMENTATION_RUN =1


MANUAL_TASK_FOLDERS = {
    "1": "task1_unique_brands",
    "2": "task2_get_average_price",
    "3": "task3_get_min_attribute",
    "4": "task4_get_reading_duration",
    "5": "task5_validate_contact_form",
    "6": "task6_validate_password",
    "7": "task7_product_list_live_v",
    "8": "task8_slugify",
    "9": "task9_product_cache_get"
}
base_dir = r"c:\Users\kalup\Desktop\Thesis"

work_directory = os.path.join(
    base_dir,
    "_execution_temp",
    "single_check"
)

manual_task_folder = MANUAL_TASK_FOLDERS[TASK_NUMBER]


if TEST_LLM.lower() == "manual":

    test_file_name = "tests.py"

    source_test_file = os.path.join(
        base_dir,
        "src",
        manual_task_folder,
        test_file_name
    )

    test_run_display = "Manual baseline"

else:
    test_file_name = f"run_{TEST_RUN:02d}_test.py"

    source_test_file = os.path.join(
        base_dir,
        "generated_tests",
        TEST_LLM,
        f"task_{TASK_NUMBER}",
        test_file_name
    )

    test_run_display = f"{TEST_RUN:02d}"



if IMPLEMENTATION_LLM.lower() == "manual":

    implementation_file_name = "implementation_manual.py"

    source_implementation_file = os.path.join(
        base_dir,
        "src",
        manual_task_folder,
        implementation_file_name
    )

    implementation_run_display = "Manual baseline"

else:
    implementation_file_name = f"run_{IMPLEMENTATION_RUN:02d}.py"

    source_implementation_file = os.path.join(
        base_dir,
        "results",
        IMPLEMENTATION_LLM,
        f"task_{TASK_NUMBER}",
        implementation_file_name
    )

    implementation_run_display = f"{IMPLEMENTATION_RUN:02d}"



if not os.path.exists(source_test_file):
    print("\nTEST FILE MISSING")
    print(source_test_file)

elif not os.path.exists(source_implementation_file):
    print("\nIMPLEMENTATION FILE MISSING")
    print(source_implementation_file)

else:
    shutil.rmtree(work_directory, ignore_errors=True)
    os.makedirs(work_directory, exist_ok=True)

    temporary_implementation_file = os.path.join(
        work_directory,
        "implementation_manual.py"
    )

    temporary_test_file = os.path.join(
        work_directory,
        "selected_test.py"
    )

    shutil.copy2(
        source_implementation_file,
        temporary_implementation_file
    )

    shutil.copy2(
        source_test_file,
        temporary_test_file
    )

    print("\n" + "=" * 75)
    print("COPY VERIFICATION")
    print("=" * 75)
    print(f"Source test suite:       {source_test_file}")
    print(f"Source implementation:   {source_implementation_file}")
    print(f"Temporary test file:     {temporary_test_file}")
    print(f"Copied implementation:   {temporary_implementation_file}")
    print("=" * 75)

    print("\n" + "=" * 75)
    print("ONE CONTROLLED TEST CHECK")
    print("=" * 75)
    print(f"Task:                    {TASK_NUMBER}")
    print(f"Test suite source:       {TEST_LLM}")
    print(f"Test suite run:          {test_run_display}")
    print(f"Implementation source:   {IMPLEMENTATION_LLM}")
    print(f"Implementation run:      {implementation_run_display}")
    print("-" * 75)
    print(f"Original test file:      {test_file_name}")
    print(f"Original impl file:      {implementation_file_name}")
    print("=" * 75 + "\n")

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "unittest",
            "-v",
            "selected_test"
        ],
        cwd=work_directory,
        capture_output=True,
        text=True,
        encoding="utf-8"
    )

    terminal_output = result.stdout + result.stderr
    print(terminal_output)

    passed_count = 0
    failed_count = 0
    error_count = 0

    for line in result.stderr.splitlines():
        line = line.strip()

        if " ... ok" in line:
            passed_count += 1

        elif " ... FAIL" in line:
            failed_count += 1

        elif " ... ERROR" in line:
            error_count += 1

    total_count = passed_count + failed_count + error_count

    print("\n" + "=" * 75)
    print("FINAL INDIVIDUAL-TEST SUMMARY")
    print("=" * 75)
    print(
        f"[{TEST_LLM} test suite, {test_run_display}] "
        f"vs "
        f"[{IMPLEMENTATION_LLM} implementation, "
        f"{implementation_run_display}]"
    )
    print(f"Passed: {passed_count}/{total_count}")
    print(f"Assertion failures: {failed_count}")
    print(f"Runtime/import errors: {error_count}")

    if result.returncode == 0:
        print("Complete?: YES")
        print("Needs investigation?: NO")
    else:
        print("Complete?: NO")
        print("Needs investigation?: YES")

    print("=" * 75 + "\n")