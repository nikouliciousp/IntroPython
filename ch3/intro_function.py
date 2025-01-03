def greet(name):
    """
    This function takes a name as input and returns a greeting message.
    
    Args:
        name (str): The name of the person to greet.
    
    Returns:
        str: A greeting message addressed to the given name.
    """
    return f"Hello, {name}!"

def add_numbers(a, b):
    """
    This function takes two numbers as input, adds them together, and returns the sum.
    
    Args:
        a (int or float): The first number.
        b (int or float): The second number.
    
    Returns:
        int or float: The sum of the two numbers.
    """
    return a + b

# Examples of using the functions
print(greet("Alice"))  # Output: Hello, Alice!
print(add_numbers(5, 7))  # Output: 12
