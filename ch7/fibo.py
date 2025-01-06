def fibonacci_recursive(n: int) -> int:
    # Base case: return n if n is 0 or 1
    if n <= 1:
        return n
    # Recursive case: calculate Fibonacci sum of the last two numbers
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def main() -> None:
    try:
        # Prompt user to input a number
        n = int(input("Enter a number to calculate its Fibonacci: "))
        if n < 0:
            # Handle negative input with a message
            print("Please enter a non-negative integer.")
        else:
            # Display the calculated Fibonacci number
            print(f"Fibonacci({n}) = {fibonacci_recursive(n)}")
    except ValueError:
        # Handle invalid input with an error message
        print("Invalid input. Please enter a valid integer.")


if __name__ == "__main__":
    # Call the main function when the script is executed
    main()
