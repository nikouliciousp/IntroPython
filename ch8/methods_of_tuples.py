# Example of count() - counts the number of occurrences of an element
my_tuple = (1, 2, 3, 2, 4, 2)
count_of_twos = my_tuple.count(2)  # Counts all occurrences of 2
print(f"Count of 2 in tuple: {count_of_twos}")  # Expected Output: 3

# Example of index() - returns the first index of an element
my_tuple = (10, 20, 30, 20, 40)
index_of_20 = my_tuple.index(20)  # Finds the first occurrence of 20
print(f"First index of 20: {index_of_20}")  # Expected Output: 1

# Example of a ValueError - demonstrates handling an invalid index lookup
my_tuple = (10, 20, 30, 20, 40)
try:
    my_tuple.index(50)  # 50 is not in the tuple, raise ValueError
except ValueError as e:
    print(f"Error: {e}")  # Prints the error message

# Tuples are immutable, meaning their elements cannot be changed after creation.
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # Uncommenting this will raise a TypeError when trying to modify a tuple

# Concatenation (+) - combines two tuples into one
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result = tuple1 + tuple2  # Combines both tuples
print(f"Concatenated Tuple: {result}")  # Expected Output: (1, 2, 3, 4, 5, 6)

# Repetition (*) - repeats the tuple elements multiple times
my_tuple = (1, 2, 3)
repeated = my_tuple * 3  # Repeats the tuple 3 times
print(f"Repeated Tuple: {repeated}")  # Expected Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)

# Membership Testing (in, not in) - checks if an element exists in a tuple
my_tuple = (10, 20, 30)
print(20 in my_tuple)  # True if 20 exists in the tuple, Expected Output: True
print(40 not in my_tuple)  # True if 40 does not exist in the tuple, Expected Output: True

# Iteration - loop through the elements of a tuple
my_tuple = (5, 10, 15)
for value in my_tuple:
    print(value, end=" ")  # Prints each value in the tuple
print()
# Expected Output: 5 10 15

# Length, Min, Max - built-in functions to analyze tuples
my_tuple = (1, 5, 3, 4, 2)
print(len(my_tuple))  # Length of the tuple, Expected Output: 5
print(min(my_tuple))  # Minimum value in the tuple, Expected Output: 1
print(max(my_tuple))  # Maximum value in the tuple, Expected Output: 5

# Slicing - extracts a subset of the tuple
my_tuple = (10, 20, 30, 40, 50)
sliced = my_tuple[1:4]  # Extracts elements from index 1 to 3 (exclusive of index 4)
print(f"Sliced Tuple: {sliced}")  # Expected Output: (20, 30, 40)
