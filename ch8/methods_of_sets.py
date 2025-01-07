# Example 1: Using the union() method
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_result = set1.union(set2)  # Combines elements from both sets without duplicates
print("Union:", union_result)

# Example 2: Using the intersection() method
intersection_result = set1.intersection(set2)  # Returns common elements of both sets
print("Intersection:", intersection_result)

# Example 3: Using the difference() method
difference_result = set1.difference(set2)  # Returns elements in set1 that are not in set2
print("Difference:", difference_result)

# Example 4: Using the symmetric_difference() method
symmetric_difference_result = set1.symmetric_difference(set2)  # Returns elements in either set, but not in both
print("Symmetric Difference:", symmetric_difference_result)

# Example 5: Using the issubset() method
is_subset = {1, 2}.issubset(set1)  # Checks if all elements of the subset are in set1
print("Is Subset:", is_subset)

# Example 6: Using the issuperset() method
is_superset = set1.issuperset({1, 2})  # Checks if set1 contains all elements of the given set
print("Is Superset:", is_superset)

# Example 7: Using the isdisjoint() method
is_disjoint = set1.isdisjoint({6, 7})  # Checks if set1 has no elements in common with the given set
print("Is Disjoint:", is_disjoint)

# Example 8: Using the operator |
union_result = set1 | set2  # Combines elements from both sets without duplicates
print("Union |:", union_result)

# Example 9: Using the operator &
intersection_result = set1 & set2  # Returns common elements of both sets
print("Intersection &:", intersection_result)

# Example 10: Using the operator -
difference_result = set1 - set2  # Returns elements in set1 that are not in set2
print("Difference -:", difference_result)

# Example 11: Using the operator ^
symmetric_difference_result = set1 ^ set2  # Returns elements in either set, but not in both
print("Symmetric Difference ^:", symmetric_difference_result)


