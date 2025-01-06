# Example: Using lambda and filter to filter numbers greater than 5 from a list.
# The 'filter' function is used to select elements from a collection that satisfy a condition. 
# In this case, it filters out numbers greater than 5.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
greater_than_five = list(filter(lambda x: x > 5, numbers))
print(greater_than_five)  # Output: [6, 7, 8, 9, 10]

# Example: Using lambda and map to compute squares of numbers in a list.
# The 'map' function is used to transform each element of a collection based on a specified function. 
# Here, it calculates the square of each number in the list.
squares = list(map(lambda x: x ** 2, numbers))
print(squares)  # Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

