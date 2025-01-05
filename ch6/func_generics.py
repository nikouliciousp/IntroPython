from typing import TypeVar, List

T = TypeVar('T')  # Define a type variable to use for generics

def get_first_item(items: List[T]) -> T:
    """
    Retrieves the first item from a list.
    :param items: A list of any type.
    :return: The first item in the list.
    """
    return items[0] if items else None

def compare_values(a: T, b: T) -> bool:
    """
    Compares two generic values and checks if they are equal.
    :param a: The first value.
    :param b: The second value.
    :return: True if values are equal, False otherwise.
    """
    return a == b

def main():
    """
    Demonstrates the usage of generic functions.
    """
    # Example usage of get_first_item
    numbers = [1, 2, 3, 4, 5]
    first_number = get_first_item(numbers)
    print(f"The first number is: {first_number}")

    # Example usage of compare_values
    result = compare_values(10, 10)
    print(f"Are the numbers equal? {result}")

if __name__ == "__main__":
    main()
