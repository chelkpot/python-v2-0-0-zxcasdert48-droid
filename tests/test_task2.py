import io
import sys
from tasks.task2 import solve

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
    # 2 карандаша, 3 ручки, 1 фломастер
    # 2*3 + 3*5 + 1*12 = 33
    assert run_io("2 3 1\n") == "33"

def test_case2():
    # 1 карандаш, 1 ручка, 1 фломастер
    # 1*3 + 1*5 + 1*12 = 20
    assert run_io("1 1 1\n") == "20"

def test_case3():
    # 0 карандашей, 5 ручек, 2 фломастера
    # 0*3 + 5*5 + 2*12 = 49
    assert run_io("0 5 2\n") == "49"
