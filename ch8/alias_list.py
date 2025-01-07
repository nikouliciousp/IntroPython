import copy

# Original list
my_list = [1, 2, 3]

# Alias to the same list
alias = my_list  # Both variables point to the same list object - Shallow copy

# Alias using slicing (Shallow copy)
alias2 = my_list[:]  # Creates a new list object

# Deep copy example
deep_copy = copy.deepcopy(my_list)  # Creates a completely independent copy

# Modifying the alias affects the original list
alias[0] = 4

# Modifying the alias2 does not affect the original list
alias2[1] = 5

# Modifying the deep copy does not affect the original list
deep_copy[2] = 6

# Printing the IDs and values to show they are different objects
print(f"list id: {id(my_list)}, value: {my_list}")  # Prints the id and updated value of my_list
print(f"alias id: {id(alias)}, value: {alias}")  # Prints the id and updated value of alias
print(f"alias2 id: {id(alias2)}, value: {alias2}")  # Prints the id and value of alias2 to show it's a different object
print(
    f"deep_copy id: {id(deep_copy)}, value: {deep_copy}")  # Prints the id and value of deep_copy to show it's completely independent
