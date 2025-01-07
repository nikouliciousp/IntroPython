# Examples of dictionary methods in Python

# Initializing a dictionary
example_dict = {"a": 1, "b": 2, "c": 3}
print(f"Initial dictionary: {example_dict}")

# 1. Accessing a value with .get()
value = example_dict.get("a", "Default value")  # Returns 1
print(f"Value of 'a': {value}")

# 2. Getting all keys with .keys()
keys = example_dict.keys()  # Returns dict_keys(['a', 'b', 'c'])
print(f"Keys of the dictionary: {keys}")

# 3. Getting all values with .values()
values = example_dict.values()  # Returns dict_values([1, 2, 3])
print(f"Values of the dictionary: {values}")

# 4. Getting all key-value pairs with .items()
items = example_dict.items()  # Returns dict_items([('a', 1), ('b', 2), ('c', 3)])
print(f"Key-value pairs of the dictionary: {items}")

# 5. Updating a dictionary with .update()
example_dict.update({"d": 4})  # example_dict becomes {'a': 1, 'b': 2, 'c': 3, 'd': 4}
print(f"Updated dictionary: {example_dict}")

# 6. Clearing all elements from a dictionary with .clear()
temp_dict = example_dict.copy()  # Making a copy for demonstration
temp_dict.clear()  # temp_dict becomes {}
print(f"Cleared dictionary: {temp_dict}")

# 7. Removing a specific key-value pair with .pop()
removed_value = example_dict.pop("a")  # Removes key 'a' and returns its value (1)
print(f"Removed value: {removed_value}")

# 8. Removing and returning a random key-value pair with .popitem()
removed_pair = example_dict.popitem()  # Removes and returns the last inserted pair ('d', 4)
print(f"Removed pair: {removed_pair}")

# 9. Setting a default value with .setdefault()
default_value = example_dict.setdefault("e", 5)  # Adds key 'e' with value 5 if not present
print(f"Default value: {default_value}")

# 10. Creating a new dictionary from keys with .fromkeys()
keys_list = ["x", "y", "z"]
new_dict = dict.fromkeys(keys_list, 0)  # Creates {'x': 0, 'y': 0, 'z': 0}
print(f"New dictionary: {new_dict}")

# 11. Creating a shallow copy with .copy()
shallow_copy = example_dict.copy()  # Creates a shallow copy of the dictionary
print(f"Shallow copy: {shallow_copy}")
