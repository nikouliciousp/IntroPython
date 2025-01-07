import functools


def calculate_operations(args):
    # Convert arguments to float for computations
    args = list(map(float, args))  # Convert to list so it can be reused in multiple operations

    # Function to perform addition
    def plus():
        return functools.reduce(lambda x, y: x + y, args)

    # Function to perform subtraction
    def minus():
        return functools.reduce(lambda x, y: x - y, args)

    # Function to perform multiplication
    def multiply():
        return functools.reduce(lambda x, y: x * y, args)

    # Function to perform division
    def divide():
        if 0 in args[1:]:  # Check if any value other than the first is zero
            raise ValueError("Cannot divide by zero.")
        return functools.reduce(lambda x, y: x / y, args)

    # Function to calculate exponentiation
    def exponent():
        return functools.reduce(lambda x, y: x ** y, args)

    # Function to perform root operation
    def root():
        for x, y in zip(args[:-1], args[1:]):  # Iterate over pairs of arguments
            if y == 0:
                raise ValueError("Cannot take the root with exponent 0.")
            if x < 0 and y % 2 == 0:  # Check for invalid even root of negative number
                raise ValueError("Cannot compute even root of a negative number.")
        return functools.reduce(lambda x, y: x ** (1 / y), args)

    # Function to calculate modulo operation (remainder)
    def mod():
        for y in args[1:]:  # Check subsequent arguments for zero
            if y == 0:
                raise ValueError("Cannot compute modulo by zero.")
        return functools.reduce(lambda x, y: x % y, args)

    # Return a dictionary of all possible operations
    return {
        "plus": plus,
        "minus": minus,
        "multiply": multiply,
        "divide": divide,
        "exponent": exponent,
        "root": root,
        "mod": mod,
    }

def main():
    args = input("Enter numbers separated by space: ").split()
    operation = input("Enter the operation (plus, minus, multiply, divide, exponent, root, mod): ").strip()
    operations = calculate_operations(args)

    if operation in operations:
        try:
            result = operations[operation]()
            print(f"The result of {operation} is: {result}")
        except Exception as e:
            print(f"An error occurred while performing the operation: {e}")
    else:
        print(f"Invalid operation: {operation}")


if __name__ == "__main__":
    main()