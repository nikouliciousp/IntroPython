# Example 1: Lambda function to square a number
square = lambda x: x ** 2
print(square(4))  # Output: 16

# Example 2: Lambda function to filter even numbers from a list
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]

# Example 3: Lambda function to sort a list of tuples based on the second element
pairs = [(1, 3), (4, 1), (2, 2), (5, 0)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)  # Output: [(5, 0), (4, 1), (2, 2), (1, 3)]
