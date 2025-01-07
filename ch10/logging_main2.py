import logging_demo2

# Function to find the number in the list and handle logging
def find_and_log_number(nums, num_to_find):
    try:
        # Try finding the index of the number in the list
        num_index = nums.index(num_to_find)
        print(f'Found {num_to_find} at index {num_index}')  # Print success message
    except ValueError:
        # Log an error if the number is not found in the list
        logging_demo2.logger.error(
            f"Value {num_to_find} not found in list {nums}",
            exc_info=True  # Include the stack trace for debugging
        )

def main():
    # List of numbers to search in
    nums = [1, 2, 3, 4, 5]
    print(f'Searching for: {nums}')

    # The number to find in the list
    num_to_find = 20
    print(f'Searching for: {num_to_find}')

    find_and_log_number(nums, num_to_find)

if __name__ == "__main__":
    main()