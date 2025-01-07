# List
print("Lists:")
# Empty list
list1 = []
print(f"Empty list: {list1}")

# List with elements
list2 = [1, 2, 3, 4]
print(f"List with elements: {list2}")

# Using the `list()` function
list3 = list()  # Empty list
list4 = list((5, 6, 7))  # With elements from a tuple
print(f"Empty list: {list3}")
print(f"")

# Mixing data types
list5 = [1, "string", 3.14, True]
print(f"List with mixed data types: {list5}")

# List from generator expression
list6 = [x ** 2 for x in range(5)]  # [0, 1, 4, 9, 16]
print(f"List from generator expression: {list6}")

# List from tuple
list7 = list((10, "true", 3.14, False))
print(f"List from tuple: {list7}")

# Dynamic list
#list8 = eval(input("Enter a list (e.g., [1, 2, 3]): "))
list8 = eval("[1, 2, 3]")
print(f"List from user input: {list8}")

# List from string
string = "abc"
list9 = list(string)
print(f"List from string: {list9}")

# List from range
list10 = list(range(5))
print(f"List from range: {list10}")

# List from split
string2 = "a b c"
list11 = string2.split()
print(f"Split string: {list11}")

# Tuples
print("\nTuples:")
# Empty tuple
tuple1 = ()
print(f"Empty tuple: {tuple1}")

# Tuple with elements
tuple2 = (1, 2, 3, 4)
print(f"Tuple with elements: {tuple2}")

# Using the `tuple()` function
tuple3 = tuple()  # Empty tuple
tuple4 = tuple([5, 6, 7])  # From a list
print(f"Empty tuple: {tuple3}")
print(f"Tuple from list: {tuple4}")

# Single element (requires a comma)
tuple5 = (42,)  # Correct syntax
print(f"Single element tuple: {tuple5}")
tuple6 = 42  # Not a tuple, just an integer
print(f"Single element tuple: {tuple6}")

# Mixing data types
tuple7 = (1, "string", 3.14, True)
print(f"Tuple with mixed data types: {tuple7}")

# Tuple from generator expression
tuple8 = tuple(x ** 2 for x in range(5))  # (0, 1, 4, 9, 16)
print(f"Tuple from generator expression: {tuple8}")

# Frozen Sets
print("\nFrozen Sets:")
# Empty frozen set
frozen_set1 = frozenset()
print(f"Empty frozen set: {frozen_set1}")

# Frozen set with elements
frozen_set2 = frozenset([1, 2, 3, 4])
print(f"Frozen set with elements: {frozen_set2}")

# From a set
frozen_set3 = frozenset({5, 6, 7})
print(f"Frozen set from set: {frozen_set3}")

# From a string
frozen_set4 = frozenset("abc")  # {'a', 'b', 'c'}
print(f"Frozen set from string: {frozen_set4}")

# Frozen set from generator expression
frozen_set5 = frozenset(x ** 2 for x in range(5))  # {0, 1, 4, 9, 16}
print(f"Frozen set from generator expression: {frozen_set5}")

# Dictionaries
print("\nDictionaries:")
# Empty dictionary
dict1 = {}
print(f"Empty dictionary: {dict1}")

# Dictionary with elements
dict2 = {"a": 1, "b": 2, "c": 3}
print(f"Dictionary with elements: {dict2}")

# Using the `dict()` function
dict3 = dict()  # Empty dictionary
dict4 = dict(a=1, b=2, c=3)  # Similar to {"a": 1, "b": 2, "c": 3}
print(f"Empty dictionary: {dict3}")
print(f"Dictionary from keyword arguments: {dict4}")

# Dictionary from a list or tuple of pairs
dict5 = dict([("a", 1), ("b", 2), ("c", 3)])
print(f"Dictionary from list of pairs: {dict5}")

# Dictionary from generator expression
dict6 = {x: x ** 2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print(f"Dictionary from generator expression: {dict6}")

# Mixed data types
dict7 = {"key1": 123, "key2": [1, 2, 3], "key3": {"nested": "value"}}
print(f"Dictionary with mixed data types: {dict7}")
