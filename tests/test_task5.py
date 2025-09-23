import io
import sys

def solve():
    s = input().strip()
    print(s, end=" - Сказала Гермиона!\n")

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
    assert run_io("Алохомора\n") == "Алохомора - Сказала Гермиона!"
def test_case2():
    assert run_io("Wingardium Leviosa\n") == "Wingardium Leviosa - Сказала Гермиона!"
def test_case3():
    assert run_io("Expelliarmus\n") == "Expelliarmus - Сказала Гермиона!"
