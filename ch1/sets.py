def set_examples():
    # Example 1: Create and print a set
    set1 = {1, 2, 3, 4}
    print("Initial set:", set1)

    # Example 2: Union of two sets
    set2 = {3, 4, 5, 6}
    union_set = set1.union(set2)
    print("Union of set1 and set2:", union_set)

    # Example 3: Intersection of two sets
    intersection_set = set1.intersection(set2)
    print("Intersection of set1 and set2:", intersection_set)

    # Example 4: Difference of two sets
    difference_set = set1.difference(set2)
    print("Difference of set1 and set2:", difference_set)

# Call the function
set_examples()
