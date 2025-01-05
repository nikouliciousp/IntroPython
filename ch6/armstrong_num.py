def main():
    """
    Main function to check if the input number is an Armstrong number.
    An Armstrong number (or narcissistic number) for a given number of digits
    is a number that is equal to the sum of its own digits each raised 
    to the power of the number of digits.
    """
    num = int(input("Enter a number: "))  # Add input functionality to get a number.

    # Convert number to string to calculate its digits.
    sum_of_powers = sum(int(digit) ** len(str(num)) for digit in str(num))

    # Check Armstrong condition and print result.
    if sum_of_powers == num:
        print(f"{num} is an Armstrong number.")
    else:
        print(f"{num} is not an Armstrong number.")


if __name__ == "__main__":
    main()