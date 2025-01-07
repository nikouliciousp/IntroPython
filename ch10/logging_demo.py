import logging

# Log file name where logs will be stored
log_file = 'log_file.log'

# Create a FileHandler for logging to a file
file_handler = logging.FileHandler(log_file, mode='a')

# Create a list of handlers for the logger
handlers = [file_handler]

# Create or retrieve a logger with the specified name
logger = logging.getLogger('search_logger')

# Configure the root logger with handlers and set log format and level
logging.basicConfig(
    handlers=handlers,  # Attach the list of handlers
    level=logging.INFO,  # Set logging level to INFO
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"  # Define the log format
)

# List of numbers to search in
nums = [1, 2, 3, 4, 5]

# The number to find in the list
num_to_find = 20

try:
    # Try finding the index of the number in the list
    num_index = nums.index(num_to_find)  # Search for the number's index
    print(f'Found {num_to_find} at index {num_index}')  # Print success message
except ValueError as e:
    # Log an error if the number is not found in the list
    logger.error(
        f"Value {num_to_find} not found in list {nums}",  # Log the error message
        exc_info=True  # Include the stack trace for debugging
    )
