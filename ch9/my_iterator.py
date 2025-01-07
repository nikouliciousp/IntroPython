class CustomFactoIterator:
    """
    A custom iterator to calculate the cumulative factorial product
    of a sequence of integers.

    Attributes:
        data (iterable): The sequence of integers for which factorials are calculated.
        index (int): The current index in the sequence.
        factorial (int): The running factorial product.
    """

    def __init__(self, data):
        """
        Initializes the iterator with the given data sequence.

        Args:
            data (iterable): An iterable sequence of integers.
        """
        self.data = data
        self.index = 0
        self.factorial = 1  # Initialize factorial with 1

    def __iter__(self):
        """
        Returns the iterator object itself.

        Returns:
            CustomFactoIterator: The iterator object.
        """
        return self  # The iterator object returns itself

    def __next__(self):
        """
        Calculates the next value in the cumulative factorial
        sequence and advances the iterator.

        Returns:
            int: The next cumulative factorial value.

        Raises:
            StopIteration: When all elements in the sequence are processed.
        """
        if self.index >= len(self.data):  # Check if index is out of range
            raise StopIteration  # Stop the iteration if all elements are processed
        else:
            self.factorial *= self.data[self.index]  # Update factorial
            self.index += 1  # Move to the next index
            return self.factorial  # Return the current factorial value

def main():
    """
    Main function to calculate the factorial of a number using the custom iterator.
    Prompts the user for input and prints the intermediate factorial values.
    """
    num = int(input("Enter a number to calculate its factorial: "))  # Get user input
    my_iterator = CustomFactoIterator(range(1, num + 1))  # Create an instance of the iterator
    a = 1
    for factorial in my_iterator:  # Iterate through the factorial values
        print(f"Factorial({a}) = {factorial}")
        a += 1

if __name__ == "__main__":
    main()
