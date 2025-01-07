# Demonstrating all methods of Python lists

# Creating a sample list
my_list = [1, 2, 3, 4, 5]
print("Original list:", my_list)

# 1. append() - Adds an element at the end of the list
my_list.append(6)  # my_list becomes [1, 2, 3, 4, 5, 6]
print("Appended list:", my_list)

# 2. clear() - Removes all the elements from the list
my_list.clear()  # my_list becomes []
print("Cleared list:", my_list)

# 3. copy() - Returns a shallow copy of the list
my_list = [1, 2, 3]
print("Original list:", my_list)
copied_list = my_list.copy()  # copied_list is [1, 2, 3]
print("Copied list:", copied_list)

# 4. count() - Returns the number of elements with the specified value
count = my_list.count(2)  # count is 1
print("Count of 2s:", count)

# 5. extend() - Adds all elements of an iterable to the end of the list
my_list.extend([4, 5])  # my_list becomes [1, 2, 3, 4, 5]
print("Extended list:", my_list)

# 6. index() - Returns the index of the first occurrence of a specified value
index = my_list.index(3)  # index is 2
print("Index of 3:", index)

# 7. insert() - Adds an element at a specified position
my_list.insert(2, 10)  # my_list becomes [1, 2, 10, 3, 4, 5]
print("Inserted list:", my_list)

# 8. pop() - Removes the element at a specified position and returns it
removed_element = my_list.pop(2)  # removed_element is 10, my_list becomes [1, 2, 3, 4, 5]
print("Removed element:", removed_element)

# 9. remove() - Removes the first occurrence of a specified value
my_list.remove(2)  # my_list becomes [1, 3, 4, 5]
print("Removed list:", my_list)

# 10. reverse() - Reverses the order of the list
my_list.reverse()  # my_list becomes [5, 4, 3, 1]
print("Reversed list:", my_list)

# 11. sort() - Sorts the list in ascending order by default
my_list.sort()  # my_list becomes [1, 3, 4, 5]
print("Sorted list:", my_list)

# 12. len() (not a method but commonly used) - Returns the length of the list
length = len(my_list)  # length is 4
print("Length of list:", length)