import io
import sys
from tasks.task3 import solve

def run_io(input_data: str) -> str:
    old_in, old_out = sys.stdin, sys.stdout
    sys.stdin = io.StringIO(input_data)
    sys.stdout = io.StringIO()
    try:
        solve()
        return sys.stdout.getvalue().strip()
    finally:
        sys.stdin, sys.stdout = old_in, old_out

def test_case1():
    assert run_io("3 2\n") == "1 2"

def test_case2():
    assert run_io("5 4\n") == "3 4"

def test_case3():
    assert run_io("1 1\n") == "0 0"
