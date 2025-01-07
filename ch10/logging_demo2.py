import logging

# Log file name where logs will be stored
log_file = 'log_file.log'

# Configure the logger and file handler with appropriate settings
logging.basicConfig(
    filename=log_file,  # File to save logs
    filemode='a',  # Append mode for the log file
    level=logging.INFO,  # Set logging level to INFO
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s"  # Define the log format
)

# Create or retrieve a logger with the specified name
logger = logging.getLogger('search_logger')
