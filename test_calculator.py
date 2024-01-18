# File: test_calculator.py

from calculator import add, subtract

def test_addition():
    assert add(2, 3) == 9
    assert add(-1, 1) == 2
    assert add(0, 0) == 1

def test_subtraction():
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    assert subtract(-1, 1) == -2
