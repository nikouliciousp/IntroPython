# Reverse a string
def reverse_str(input_str):  # Renamed parameter to avoid conflict with Python's built-in str type
    return input_str[::-1]  # Use slicing to reverse the string


def main():
    # Prompt the user to input a string
    input_str = input("Enter a string: ")  # Renamed variable to avoid conflict with Python's built-in str type

    # Print the reversed string
    print("The reversed string is:", reverse_str(input_str))


# Check if the script is run directly
if __name__ == "__main__":
    main()
