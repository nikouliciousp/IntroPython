def fub_add(a: int | float, b: int | float) -> int | float:
    """
    Adds two numeric values and returns the result.

    This function takes two numeric inputs, either of type int or float,
    and computes their sum. If either of the inputs is not numeric,
    it raises a ValueError.

    :return: The sum of `a` and `b`.
    :rtype: int | float
    :raises ValueError: If either of the inputs is not a numeric value.
    """
    if not isinstance(a, (int, float)):
        raise ValueError(f"Invalid input for 'a': expected int or float, got {type(a).__name__}")
    if not isinstance(b, (int, float)):
        raise ValueError(f"Invalid input for 'b': expected int or float, got {type(b).__name__}")
    return a + b


if __name__ == "__main__":
    while True:
        try:
            a = input("Enter a number: ").strip()
            b = input("Enter another number: ").strip()
            a = float(a) if '.' in a else int(a)
            b = float(b) if '.' in b else int(b)
            result = fub_add(a, b)
            print("Result:", result)
            print("Annotations:", fub_add.__annotations__)
            print("Docstring:", fub_add.__doc__)
            break
        except ValueError as e:
            print("Error:", e)
            print("Invalid input! Please enter a numeric value.")
