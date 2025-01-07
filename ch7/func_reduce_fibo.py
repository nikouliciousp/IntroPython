from functools import reduce

def fibonacci_with_reduce(n):
    """
    Calculate the nth Fibonacci number using reduce.
    :param n: Index of the Fibonacci number (0-based).
    :return: The nth Fibonacci number.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
  
    # Use reduce to calculate the Fibonacci series up to nth number
    return reduce(lambda x, _: (x[1], x[0] + x[1]), range(n - 1), (0, 1))[1]

def main():
    try:
        user_input = int(input("Enter the index of the Fibonacci number: "))
        result = fibonacci_with_reduce(user_input)
        print(f"The {user_input}th Fibonacci number is: {result}")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()