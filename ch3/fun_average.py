# Function to calculate the average of a list of numbers
def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    Args:
        numbers (list): A list of numeric values.

    Returns:
        float: The average value of the numbers in the list.
               Returns None if the list is empty.
    """
    if not numbers:  # Check if the list is empty
        return None
    return sum(numbers) / len(numbers)


def main():
    """
    Main function to handle user input and calculate the average.
    """
    try:
        input_numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
        average = calculate_average(input_numbers)
        if average is None:
            print("The list is empty. No average to calculate.")
        else:
            print(f"The average of {input_numbers} is {average}")
    except ValueError:
        print("Invalid input. Please enter numbers only.")


if __name__ == "__main__":
    print("Average Calculator")
    print(calculate_average.__doc__)
    main()
