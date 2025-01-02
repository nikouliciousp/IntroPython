# Example 1: Range with a single argument (stops at 5, exclusive)
for i in range(5):
    print(i)

# Example 2: Range with a start and stop argument (starts at 2, stops at 5, exclusive)
for i in range(2, 5):
    print(i)

# Example 3: Range with start, stop, and step arguments (starts at 2, stops at 10, step is 2)
for i in range(2, 10, 2):
    print(i)

# Example 4: Range with negative step (counts down from 10 to 1, inclusive of 10 but exclusive of 1)
for i in range(10, 1, -2):
    print(i)

# Example 5: Creating a list from range (list output displayed)
print(list(range(5)))

# Example 6: Using range in a sum function (sums integers 0 through 4)
print(sum(range(5)))
