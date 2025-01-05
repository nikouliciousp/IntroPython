"""
This script provides a function to take user input and print it with spaces between each character.
"""

def print_with_spaces():
    """
    This function takes input from the user, adds spaces between each character,
    and prints the modified string.
    """
    user_input = input("Enter a string: ")
    spaced_output = " ".join(user_input)
    print(spaced_output)

if __name__ == "__main__":
    print_with_spaces()