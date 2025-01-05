def fibonacci(n):
    """Calculate Fibonacci number recursively."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    """Main function for the Fibonacci app."""
    while True:
        user_input = input("Enter the position of the Fibonacci number you wish to calculate: ")
        if user_input.isdigit():
            n = int(user_input)
            break
        else:
            print("Invalid input. Please enter a positive integer.")
    print(f"The Fibonacci number at position {n} is {fibonacci(n)}.")

if __name__ == "__main__":
    main()
