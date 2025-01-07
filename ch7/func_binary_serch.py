# Binary Search
def binary_search(my_list, item, start, end):
    # Base case: item not found
    if start > end:
        return False
    else:
        # Calculate the mid-point index
        mid = (start + end) // 2
        # Check if the middle element is the item
        if my_list[mid] == item:
            return True
        # If item is smaller, search in the left half
        elif my_list[mid] > item:
            return binary_search(my_list, item, start, mid - 1)
        # If item is larger, search in the right half
        else:
            return binary_search(my_list, item, mid + 1, end)


def main():
    # Define a sample sorted list
    my_list = [1, 3, 5, 7, 9]
    # Get the target item to search from user input
    item = int(input("Enter the number you wish to search for: "))
    # Perform binary search on the list
    result = binary_search(my_list, item, 0, len(my_list) - 1)
    # Display the result
    if result:
        print(f"{item} is in the list.")
    else:
        print(f"{item} is not in the list.")


if __name__ == "__main__":
    main()
