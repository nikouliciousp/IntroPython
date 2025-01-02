# Explain the concept of hash-ability in Python data structures with examples

# Hash-ability determines if an object can be used as keys in a dictionary or as elements in a set.
# To be hashable, objects must have a fixed hash value during their lifetime and implement __hash__() and __eq__().

# 1. List: Lists are mutable, so they are NOT hashable.
try:
    hash([])  # Trying to hash a list
    print("Lists are hashable.")
except TypeError:
    print("Lists are NOT hashable.")

# 2. Set: Sets are also mutable, so they are NOT hashable.
try:
    hash(set())  # Trying to hash a set
    print("Sets are hashable.")
except TypeError:
    print("Sets are NOT hashable.")

# 3. Tuple: Tuples are immutable and hashable *if* all their elements are hashable.
try:
    print("Tuples are hashable:", hash((1, 2, 3)))  # This works
    hash((1, [2], 3))  # This fails because a list inside makes it non-hashable
except TypeError:
    print("Tuples are NOT hashable if they contain mutable objects.")

# 4. Frozenset: Frozen-sets are immutable and hashable because they cannot change after creation.
try:
    print("Frozensets are hashable:", hash(frozenset([1, 2, 3])))
except TypeError:
    print("Frozensets are NOT hashable.")

# 5. Dictionary: Keys in a dictionary must be hashable; however, dictionaries themselves are mutable and NOT hashable.
try:
    hash({})  # Trying to hash a dictionary
    print("Dictionaries are hashable.")
except TypeError:
    print("Dictionaries are NOT hashable.")

# Example: Using hashable objects as keys in dictionaries or as elements in sets
example_dict = {}
example_set = set()

# Using a tuple and frozenset as dictionary keys (works because both are hashable)
example_dict[(1, 2)] = "Tuple is hashable"
example_dict[frozenset([3, 4])] = "Frozenset is hashable"

# Printing the final dictionary to verify
print(example_dict)

# Attempting to use a list as a dictionary key or set element (raises TypeError)
try:
    example_dict[[]] = "List is not hashable"
except TypeError:
    print("Cannot use a list as a dictionary key because it is NOT hashable.")

try:
    example_set.add([])  # Fails
except TypeError:
    print("Cannot add a list to a set because it is NOT hashable.")
