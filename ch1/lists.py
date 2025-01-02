def populate_list_with_range():
    example_list = list(range(10))  # Creates a list of numbers from 0 to 9
    print(example_list)

def populate_list_with_comprehension():
    example_list = [x**2 for x in range(10)]  # Creates a list of squares of numbers from 0 to 9
    print(example_list)

def populate_list_manually():
    example_list = []  # Start with an empty list
    example_list.append(1)
    example_list.append(2)
    example_list.append(3)
    print(example_list)

def iterate_list_with_index_and_value():
    example_list = ["a", "b", "c"]  # Example list to test index and value iteration
    for index, value in enumerate(example_list):
        print(f"Index: {index}, Value: {value}")

populate_list_with_range()
populate_list_with_comprehension()
populate_list_manually()
iterate_list_with_index_and_value()