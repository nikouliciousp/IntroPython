def factorial():
    """
    A generator function to compute the factorial of numbers incrementally.

    Yields:
        int: The next factorial in the sequence.
    """
    n, result = 0, 1
    while True:
        yield result
        n += 1
        result *= n

def main():
    """
    Main function to demonstrate the factorial generator by printing
    the first nth factorials of user input.
    """
    try:
        count = int(input("Enter the number of factorials to print: "))
        if count < 0:
            print("Please enter a non-negative integer.")
            return
        facto = factorial()
        for i in range(count):
            print(f"Factorial {i}: {next(facto)}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()