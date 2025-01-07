class IterFactorial:
    """
    An iterator class to compute the factorial of numbers from 1 to n iteratively.
    """

    def __init__(self, n):
        """
        Initialize the iterator with a limit `n`.

        :param n: The upper limit for factorial computation.
        """
        self.n = n
        self.order = 1
        self.factorial = 1

    def __iter__(self):
        """
        Return the iterator object itself.
        """
        return self

    def __next__(self):
        """
        Compute the next factorial in the sequence.

        :raises StopIteration: If the current number exceeds the limit `n`.
        :return: The factorial of the current number in the sequence.
        """
        if self.order > self.n:
            raise StopIteration
        else:
            self.factorial *= self.order
            self.order += 1
            return self.factorial

def main():
    """
    Main function to iterate over the factorials and print them.
    """
    # Get user input for the upper limit `n` for the factorial sequence
    facto = iter(IterFactorial(int(input("Enter a number: "))))

    # Iterate through the generated factorials and print each with a formatted output
    for i in facto:
        print("{:,}".format(i))  # Print factorial with thousands separator for better readability


if __name__ == '__main__':
    main()
