def add_numbers(a, b):
    """
    Demonstrates addition of two numbers.
    """
    result = a + b
    print(f"The result of addition is: {result}")
    return result


def subtract_numbers(a, b):
    """
    Demonstrates subtraction of two numbers.
    """
    result = a - b
    print(f"The result of subtraction is: {result}")
    return result


def multiply_numbers(a, b):
    """
    Demonstrates multiplication of two numbers.
    """
    result = a * b
    print(f"The result of multiplication is: {result}")
    return result


def divide_numbers(a, b):
    """
    Demonstrates division of two numbers.
    """
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    result = a / b
    print(f"The result of division is: {result}")
    return result


def modulo_numbers(a, b):
    """
    Demonstrates the modulo operation.
    """
    if b == 0:
        raise ValueError("Modulo by zero is not allowed.")
    result = a % b
    print(f"The result of modulo is: {result}")
    return result


def exponential_numbers(a, b):
    """
    Demonstrates exponentiation of a number.
    """
    result = a ** b
    print(f"The result of exponentiation is: {result}")
    return result

add_numbers(5, 3)
subtract_numbers(10, 4)
multiply_numbers(7, 6)
divide_numbers(8, 2)
modulo_numbers(10, 3)
exponential_numbers(2, 3)