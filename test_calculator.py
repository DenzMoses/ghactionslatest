# File: test_calculator.py

from calculator import add, subtract, multiply, divide

def test_addition():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtraction():
    assert subtract(5, 3) == 2
    assert subtract(0, 0) == 0
    assert subtract(-1, 1) == -2

def test_multiplication():
    assert multiply(2, 3) == 6
    assert multiply(-1, 1) == -1
    assert multiply(0, 0) == 0

def test_division():
    assert divide(6, 2) == 3
    assert divide(-10, 2) == -5

def test_division_by_zero():
    try:
        divide(6, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"

