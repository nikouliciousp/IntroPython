num = 10  # Assign the integer value 10 to the variable 'num'
my_list = [1, 2, 3]  # Assign a list containing the integers 1, 2, and 3 to 'my_list'

print(id(num))  # Print the memory address of the object referenced by 'num'
print(id(10))  # Print the memory address of the integer object 10 (due to interning)

print(id(my_list))  # Print the memory address of the object referenced by 'my_list'
print(id([1, 2, 3]))  # Print the memory address of a newly created list object with the same values
print(my_list is [1, 2, 3])  # Check if 'my_list' and a new list [1, 2, 3] refer to the same object
