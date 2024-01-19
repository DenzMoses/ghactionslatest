# File: calculator.py
#add
def add(x, y):
    result = x + y
    print(f"{x} + {y} = {result}")
    return result

def subtract(x, y):
    result = x - y
    print(f"{x} - {y} = {result}")
    return result

def multiply(x, y):
    result = x * y
    print(f"{x} * {y} = {result}")
    return result

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    result = x / y
    print(f"{x} / {y} = {result}")
    return result
