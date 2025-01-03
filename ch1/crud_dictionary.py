def create_dictionary():
    # Create a dictionary with initial values
    my_dict = {"name": "Alice", "age": 25, "city": "New York"}
    print("Created Dictionary:", my_dict)
    return my_dict

def read_from_dictionary(my_dict, key):
    # Read a value by key from the dictionary
    value = my_dict.get(key, "Key not found")
    print(f"Read from Dictionary: Key='{key}', Value='{value}'")
    return value

def update_dictionary(my_dict, key, value):
    # Update or add a key-value pair to the dictionary
    my_dict[key] = value
    print(f"Updated Dictionary: Set Key='{key}' -> Value='{value}'")
    return my_dict

def delete_from_dictionary(my_dict, key):
    # Delete a key-value pair from the dictionary
    if key in my_dict:
        del my_dict[key]
        print(f"Deleted from Dictionary: Key='{key}'")
    else:
        print(f"Delete Failed: Key='{key}' not found")
    return my_dict

# Example usage
dictionary = create_dictionary()
read_from_dictionary(dictionary, "name")
update_dictionary(dictionary, "age", 30)
update_dictionary(dictionary, "country", "USA")
delete_from_dictionary(dictionary, "city")
delete_from_dictionary(dictionary, "unknown_key")
print("Final Dictionary:", dictionary)