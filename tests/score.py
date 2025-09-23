import pytest

test_files = [
    "tests/test_task1.py",
    "tests/test_task2.py",
    "tests/test_task3.py",
    "tests/test_task4.py",
    "tests/test_task5.py"
]

def main():
    total = len(test_files)
    passed = 0
    failed_tasks = []

    for test_file in test_files:
        result = pytest.main([test_file, "--tb=no", "-q"])
        if result == 0:
            passed += 1
        else:
            failed_tasks.append(test_file.split("/")[-1])

    percent = (passed / total) * 100
    print(f"\nПроцент выполнения: {percent:.0f}%")
    if failed_tasks:
        print("Задачи с ошибками:", ", ".join(failed_tasks))
    else:
        print("Все задачи сданы ✅")

if __name__ == "__main__":
    main()
