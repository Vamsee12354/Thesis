import os
import shutil
import subprocess
import sys

task_number = "8"
# manual, gemma, deepseek, mistral, openai, amazon
test_llm = "deepseek"
# manual, gemma, deepseek, mistral, openai, amazon
impl_llm = "deepseek"
test_run = 10
impl_run = 10


manual_task_folders = {
    "1": "task1_unique_brands",
    "2": "task2_get_average_price",
    "3": "task3_get_min_attribute",
    "4": "task4_get_reading_duration",
    "5": "task5_validate_contact_form",
    "6": "task6_validate_password",
    "7": "task7_product_list_live_v",
    "8": "task8_slugify",
    "9": "task9_product_cache_get",
}

base_dir = r"c:\Users\kalup\Desktop\Thesis"

work_directory = os.path.join(
    base_dir,
    "_execution_temp",
    "single_check",
)

manual_task_folder = manual_task_folders[task_number]


if test_llm.lower() == "manual":
    test_file_name = "tests.py"

    source_test_file = os.path.join(
        base_dir,
        "src",
        manual_task_folder,
        test_file_name,
    )

    test_run_display = "manual baseline"
else:
    test_file_name = f"run_{test_run:02d}_test.py"

    source_test_file = os.path.join(
        base_dir,
        "generated_tests",
        test_llm,
        f"task_{task_number}",
        test_file_name,
    )

    test_run_display = f"{test_run:02d}"


if impl_llm.lower() == "manual":
    implementation_file_name = "implementation_manual.py"

    source_implementation_file = os.path.join(
        base_dir,
        "src",
        manual_task_folder,
        implementation_file_name,
    )

    impl_run_display = "manual baseline"
else:
    implementation_file_name = f"run_{impl_run:02d}.py"

    source_implementation_file = os.path.join(
        base_dir,
        "results",
        impl_llm,
        f"task_{task_number}",
        implementation_file_name,
    )

    impl_run_display = f"{impl_run:02d}"


if not os.path.exists(source_test_file):
    print("\ntest file missing")
    print(source_test_file)

elif not os.path.exists(source_implementation_file):
    print("\nimplementation file missing")
    print(source_implementation_file)

else:
    shutil.rmtree(work_directory, ignore_errors=True)
    os.makedirs(work_directory, exist_ok=True)

    tmp_impl_file = os.path.join(
        work_directory,
        "implementation_manual.py",
    )

    tmp_test_file = os.path.join(
        work_directory,
        "selected_test.py",
    )

    shutil.copy2(source_implementation_file, tmp_impl_file)

    shutil.copy2(source_test_file, tmp_test_file)

    print("\n" + "="*75)
    print("copy verification")
    print("="*75)
    print(f"source test suite:      {source_test_file}")
    print(f"source implementation:  {source_implementation_file}")
    print(f"temporary test file:    {tmp_test_file}")
    print(f"copied implementation:  {tmp_impl_file}")
    print("="*75)

    print( "\n" + "="*75)
    print("one controlled test check")
    print("="*75)
    print(f"task:                   {task_number}")
    print(f"test suite source:      {test_llm}")
    print(f"test suite run:         {test_run_display}")
    print(f"implementation source:  {impl_llm}")
    print(f"implementation run:     {impl_run_display}")
    print("-"*75)
    print(f"original test file:     {test_file_name}")
    print(f"original impl file:     {implementation_file_name}")
    print("="*75 + "\n")

    result = subprocess.run(
        [sys.executable, "-m", "unittest", "-v", "selected_test"],
        cwd=work_directory,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )

    terminal_output = result.stdout + result.stderr
    print(terminal_output)

    passed_count = 0
    failed_count = 0
    error_count = 0

    for line in result.stderr.splitlines():
        line = line.strip()

        if line.endswith(" ... ok"):
            passed_count += 1
        elif line.endswith(" ... FAIL"):
            failed_count += 1
        elif line.endswith(" ... ERROR"):
            error_count += 1

    total_count = passed_count + failed_count + error_count

    print("\n" + "="*75)
    print("final individual-test summary")
    print("="*75)
    print(
        f"[{test_llm} test suite, {test_run_display}] "
        f"vs "
        f"[{impl_llm} implementation, "
        f"{impl_run_display}]"
    )
    print(f"passed: {passed_count}/{total_count}")
    print(f"assertion failures:  {failed_count}")
    print(f"runtime/import errors: {error_count}")

    if result.returncode == 0:
        print("complete?: yes")
        print("needs investigation?: no")
    else:
        print("complete?: no")
        print("needs investigation?: yes")

    print("="*75 + "\n")