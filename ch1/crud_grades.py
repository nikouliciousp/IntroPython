# Define the list to hold degrees
degrees = []

# Create: Add a degree to the list
def add_degree(degree):
    degrees.append(degree)
    return f"Degree {degree} added successfully."

# Read: Retrieve all degrees or a specific degree
def get_degrees():
    return degrees

def get_degree_by_index(index):
    if 0 <= index < len(degrees):
        return degrees[index]
    else:
        return "Invalid index."

# Update: Modify a degree at a specific index
def update_degree(index, new_degree):
    if 0 <= index < len(degrees):
        old_degree = degrees[index]
        degrees[index] = new_degree
        return f"Degree at index {index} updated from {old_degree} to {new_degree}."
    else:
        return "Invalid index."

# Delete: Remove a degree from a specific index
def delete_degree(index):
    if 0 <= index < len(degrees):
        removed_degree = degrees.pop(index)
        return f"Degree {removed_degree} removed from list."
    else:
        return "Invalid index."

# Example usage to print results
def print_crud_operations():
    print(add_degree(85))
    print(add_degree(90))
    print(add_degree(75))
    print("All degrees:", get_degrees())
    print("Degree at index 1:", get_degree_by_index(1))
    print(update_degree(1, 95))
    print("All degrees after update:", get_degrees())
    print(delete_degree(0))
    print("All degrees after deletion:", get_degrees())

# Invoke example operations
if __name__ == "__main__":
    print_crud_operations()