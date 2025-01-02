# Example 1: Creating a tuple and printing its elements
example_tuple = (1, 2, 3, 4, 5)
print("Tuple elements:", example_tuple)

# Example 2: Unpacking a tuple into variables
a, b, c, d, e = example_tuple
print("Unpacked variables:", a, b, c, d, e)

# Example 3: Tuple with multiple data types
mixed_tuple = (10, "hello", 3.14, True)
print("Mixed type tuple:", mixed_tuple)

# Example 4: Nested tuple and accessing its elements
nested_tuple = ((1, 2), (3, 4), (5, 6))
print("Nested tuple:", nested_tuple)
print("Accessing nested tuple elements:", nested_tuple[0][1], nested_tuple[2][0])

# Example 5: Traversing a tuple using a for loop
print("Traversing tuple with for loop:", end=" ")
for element in example_tuple:
    print(element, end=" ")
print()

# Example 6: Traversing a tuple with index using enumerate
print("Traversing tuple with enumerate:")
for index, element in enumerate(example_tuple):
    print(f"Index {index} -> Element {element}")

