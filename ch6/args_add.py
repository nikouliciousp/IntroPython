def add(*args):
    # Initialize the total sum to 0
    total = 0
    # Iterate through all arguments and add them to the total
    for arg in args:
        total += arg
    # Return the final total
    return total


# Define the main function
def main():
    # Test the add function with some numbers
    print(add(1, 2, 3, 4, 5))


# Call main if the script is run directly
if __name__ == "__main__":
    main()
