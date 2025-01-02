# Example 1: Creating a dictionary and accessing a value
fruits = {"apple": 2, "banana": 1, "cherry": 3}
print("Price of an apple:", fruits["apple"])

# Example 2: Iterating through a dictionary and printing its key-value pairs
print("All fruits and their prices:")
for fruit, price in fruits.items():
    print(fruit, ":", price)

# Example 3: Updating the price of an existing fruit
fruits["banana"] = 2
print("Updated prices:", fruits)

# Example 4: Removing a fruit from the dictionary
del fruits["cherry"]
print("Final dictionary after removing cherry:", fruits)
