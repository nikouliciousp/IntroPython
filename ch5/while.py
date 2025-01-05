# Example 1: Basic while loop counting from 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1

# Example 2: Using while loop with break statement
i = 1
while True:
    print(f"Counting: {i}")
    if i == 5:
        break
    i += 1

# Example 3: Iterating over a list with while loop
items = ["apple", "banana", "cherry"]
index = 0
while index < len(items):
    print(f"Item: {items[index]}")
    index += 1
