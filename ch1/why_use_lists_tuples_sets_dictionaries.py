"""
This script explains the primary use cases and advantages of the following data structures in Python:
- Lists
- Tuples
- Dictionaries
- Sets
Each section includes a description and an example of each type.
"""

# List: A list is an ordered, mutable, and indexable collection of items. 
# It allows duplicate elements and is ideal for storing dynamic datasets.

# Example of using a list:
example_list = [1, 2, 3, 4]
example_list.append(5)  # Add a new item to the list
print("List example:", example_list)

# Tuple: A tuple is an ordered and immutable collection of items. 
# It is typically used for fixed datasets where data integrity is crucial.

# Example of using a tuple:
example_tuple = (10, 20, 30, 40)
print("Tuple example:", example_tuple)

# Dictionary: A dictionary is an unordered, mutable, key-value pair collection. 
# It is used for fast lookups and mapping relationships between keys and values.

# Example of using a dictionary:
example_dict = {"name": "Alice", "age": 25, "location": "Wonderland"}
example_dict["occupation"] = "Adventurer"  # Add a new key-value pair
print("Dictionary example:", example_dict)

# Set: A set is an unordered collection of unique elements. 
# It is used for membership tests and removing duplicates from collections.

# Example of using a set:
example_set = {1, 2, 3, 4, 4, 5}  # Duplicates are automatically removed
example_set.add(6)  # Add a new element to the set
print("Set example:", example_set)
