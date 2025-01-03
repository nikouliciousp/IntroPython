def traverse_dictionary():
    # Sample dictionary
    example_dict = {"a": 1, "b": 2, "c": 3}

    print("Traversing keys directly:")
    for key in example_dict:
        print(key)

    print("\nUsing .keys():")
    for key in example_dict.keys():
        print(key)

    print("\nTraversing values using .values():")
    for value in example_dict.values():
        print(value)

    print("\nTraversing key-value pairs using .items():")
    for key, value in example_dict.items():
        print(f"{key}: {value}")

    print("\nEnumerating keys (index, key):")
    for index, key in enumerate(example_dict):
        print(f"{index}: {key}")

# Call the function
traverse_dictionary()
