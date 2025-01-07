import functools


# Function to calculate the total sum of a list of money values
def calculate_total(money_list):
    # Use functools.reduce to sum up all the values in the list
    # reduce applies the lambda function cumulatively to the items in the list, 
    # taking the first two elements, then applying to the result and the next, and so on.
    return functools.reduce(lambda x, y: x + y, money_list)


def main():
    # List of money values
    money_list = [100, 200, 300]
    print(f"Money List: {money_list}")

    # Calculate the total using the calculate_total function
    total = calculate_total(money_list)

    # Print the total amount
    print(f"Total: ${total}")


# Entry point for the script
if __name__ == "__main__":
    main()
