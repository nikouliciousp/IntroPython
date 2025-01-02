# Example 1: Using enumerate to iterate through a list with indexes
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index {index} has fruit {fruit}")

# Example 2: Using enumerate with a custom starting index
animals = ["cat", "dog", "rabbit"]
for index, animal in enumerate(animals, start=1):
    print(f"Position {index}: {animal}")

# Example 3: Demonstrating enumerate in a for loop with tuples
colors = ["red", "blue", "green"]
for item in enumerate(colors):
    print(item)  # Prints a tuple of (index, value)