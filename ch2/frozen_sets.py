# Example of creating and using frozen sets
# Frozenset is an immutable version of a Python set. Unlike regular sets, 
# frozensets cannot be modified after they are created (no elements can 
# be added or removed). This makes them hashable and suitable for use 
# as dictionary keys or elements of another set.
# Use frozensets when you need a set-like data structure that must be immutable.

# Example 1: Using frozenset as a dictionary key
frozenset_key = frozenset([1, 2, 3])
my_dict = {frozenset_key: "Value associated with frozenset"}
print("Dictionary with frozenset key:", my_dict)

# Example 2: Storing frozensets in a set
set_of_frozensets = {frozenset([1, 2]), frozenset([3, 4])}
print("Set of frozensets:", set_of_frozensets)

# Example 3: Checking immutability
immutable_set = frozenset([1, 2, 3])
try:
    immutable_set.add(4)  # This will raise an AttributeError
except AttributeError as e:
    print("Error:", e)

# Example 4: Operations on frozensets
fs1 = frozenset([1, 2, 3, 4])
fs2 = frozenset([3, 4, 5, 6])
print("Intersection:", fs1 & fs2)  # Common elements: {3, 4}
print("Union:", fs1 | fs2)  # All unique elements: {1, 2, 3, 4, 5, 6}
print("Difference:", fs1 - fs2)  # Elements in fs1 but not in fs2: {1, 2}

# Example 5: Using frozensets for duplicate-free nested collections
list_of_frozensets = [frozenset([1, 2]), frozenset([2, 3]), frozenset([1, 2])]
unique_frozensets = set(list_of_frozensets)
print("Unique frozensets from the list:", unique_frozensets)
