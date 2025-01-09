import sys
from pathlib import Path


def read_file(path):
    """
    Reads the content of a file.

    Args:
        path (Path): Path to the file to be read.

    Returns:
        str: The content of the file if read successfully.
        None: If there is an error reading the file.
    """
    try:
        with open(path, "r", encoding="utf-8") as file:  # Open the file in read mode with UTF-8 encoding
            content = file.read()
        return content  # Return the content of the file
    except OSError as e:
        print(e, file=sys.stderr)  # Print error to standard error
        return None  # Return None if an error occurs


def write_file(path, content):
    """
    Appends content to a file.

    Args:
        path (Path): Path to the file to be written to.
        content (str): The content to append to the file.
    """
    try:
        with open(path, "a", encoding="utf-8") as file:  # Open the file in append mode with UTF-8 encoding
            file.write(content + "\n")  # Write the provided content to the file, add newline
    except OSError as e:
        print(e, file=sys.stderr)  # Print error to standard error


def delete_file(path):
    """
    Deletes a file.

    Args:
        path (Path): Path to the file to be deleted.

    Returns:
        bool: True if the file was deleted successfully, False otherwise.
    """
    try:
        path.unlink()  # Delete the file
        return True  # Return True if successfully deleted
    except OSError as e:
        print(e, file=sys.stderr)  # Print error to standard error
        return False  # Return False if an error occurs


def main():
    """
    Main function to read from, write to, and delete a file.
    - Reads the content of the file and prints it.
    - Writes a test string to the file.
    - Demonstrates deleting the file.
    """

    # Path to the file
    path = Path(r"C:\Users\pirat\Documents\Projects\introPython\ch12\test.txt")

    content = read_file(path)  # Read the file's content
    if content is not None:
        print(content)  # Print the file's content
    else:
        print("File not found or could not be read.")  # Inform the user if the file cannot be read

    write_file(path, "This is a test.")  # Append a test string to the file

    if delete_file(path):  # Attempt to delete the file
        print("File deleted successfully.")  # Inform the user if deletion is successful
    else:
        print("File could not be deleted.")  # Inform the user if deletion fails


if __name__ == "__main__":
    main()
