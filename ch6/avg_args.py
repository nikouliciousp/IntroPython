def avg(*args):
    # Initialize a variable to store the sum of all arguments
    my_sum = 0
    # Iterate through all the arguments and add them to the sum
    for arg in args:
        my_sum += arg
    # Return the average by dividing the sum by the number of arguments
    return my_sum / len(args)


def main():
    # Create a list of integers
    my_list = [1, 2, 3, 4, 5]

    # Call the avg function with the unpacked list and print the result
    print(avg(*my_list))


# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()
