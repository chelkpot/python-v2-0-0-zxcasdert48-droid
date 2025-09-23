import io
import sys

def solve():
    a = input().strip()
    b = input().strip()
    c = input().strip()
    print(f"{a}---{b}---{c}")

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
    assert run_io("Да пребудет\nс тобой\nСила\n") == "Да пребудет---с тобой---Сила"
def test_case2():
    assert run_io("Белка\nкаждый год\nзапасает Орехи\n") == "Белка---каждый год---запасает Орехи"
def test_case3():
    assert run_io("Первый\nВторой\nТретий\n") == "Первый---Второй---Третий"
