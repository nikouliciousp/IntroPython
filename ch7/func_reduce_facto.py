from functools import reduce


def calculate_factorial_with_reduce(num):
    """
    Calculates the factorial using functools.reduce.

    Args:
        num (int): A non-negative integer whose factorial is to be calculated.

    Returns:
        int: The factorial of the input.
    """
    if num == 0:
        return 1
    # Calculate factorial using reduce
    return reduce(lambda x, y: x * y, range(1, num + 1), 1)


def main():
    try:
        # Prompt the user for input
        num = int(input("Enter a non-negative integer to calculate its factorial: "))
        if num < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        print(f"The factorial of {num} is {calculate_factorial_with_reduce(num)}")
    except ValueError as e:
        print(f"Invalid input: {e}")


if __name__ == "__main__":
    main()
