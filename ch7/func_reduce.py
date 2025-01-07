from functools import reduce

def main():
    my_list = [1, 2, 3, 4, 5]  # Define a list of integers
    # Use reduce to calculate the sum of all elements in the list
    print(reduce(lambda x, y: x + y, my_list))  # Print the calculated sum

if __name__ == "__main__":
    main()