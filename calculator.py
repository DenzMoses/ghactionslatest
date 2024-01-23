#Calculator12345678


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


def function_to_exclude(x, y):
    result = x * y
    return result


def function_to_exclude1(x, y):
    result = x * y
    return result


def function_to_exclude12(x, y):
    # pragma: no cover
    result = x * y
    return result


def function_to_exclude123(x, y):
    # pragma: no cover
    result = x * y
    return result


def function_to_exclude1234(x, y):
    result = x * y
    return result
