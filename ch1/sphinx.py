"""
sphinx.py
==========

This module demonstrates how to use Sphinx-style docstring comments 
for generating documentation.

Author: Peris Nik
"""

def add_numbers(a: int, b: int) -> int:
    """
    Adds two numbers together.

    :param a: The first number.
    :param b: The second number.
    :return: The sum of a and b.
    :rtype: int
    """
    return a + b


def multiply_numbers(a: int, b: int) -> int:
    """
    Multiplies two numbers together.

    :param a: The first number.
    :param b: The second number.
    :return: The product of a and b.
    :rtype: int
    """
    return a * b


if __name__ == "__main__":
    """
    Entry point for the script.
    """
    print(f"Sum: {add_numbers(3, 4)}")
    print(f"Product: {multiply_numbers(3, 4)}")