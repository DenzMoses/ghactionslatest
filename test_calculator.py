# File: test_calculator.py

from calculator import add, subtract

def test_addition():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtraction():
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    assert subtract(-1, 1) == -2

def test_failing_case():
    # This test case is intentionally made to fail
    assert add(2, 2) == 5
