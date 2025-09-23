import io
import sys

def solve():
    S = int(input())
    p = S // 6
    k = 4 * p
    s = p
    print(p, k, s)

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
    assert run_io("6\n") == "1 4 1"
def test_case2():
    assert run_io("24\n") == "4 16 4"
def test_case3():
    assert run_io("60\n") == "10 40 10"
def test_case4():
    assert run_io("12\n") == "2 8 2"
