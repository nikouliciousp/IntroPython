def custom_factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return n * custom_factorial(n - 1)


def main() -> None:
    user_input: int = int(input("Enter a number to compute its factorial: "))
    print(f"The factorial of {user_input} is {custom_factorial(user_input)}")


if __name__ == "__main__":
    main()
