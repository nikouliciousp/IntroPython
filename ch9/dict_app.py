from functools import reduce

def filtering_sales(d):
    """
    Filters a dictionary to include only items where the value is greater than 100.

    Args:
        d (dict): The dictionary to filter.

    Returns:
        dict: A new dictionary with filtered items.
    """
    # Use a dictionary comprehension to filter items with values greater than 100
    filter_sales = {k: v for k, v in d.items() if v > 100}
    return filter_sales

def taxing_sales(d):
    """
    Applies a 10% tax to all sales in the dictionary using reduce.

    Args:
        d (dict): The sales dictionary.

    Returns:
        dict: A new dictionary with taxed sales values.
    """
    # Use reduce to calculate sales with taxes
    return {k: reduce(lambda x, _: x + x * 0.1, range(1), v) for k, v in d.items()}
    

def main():
    """
    Main function to create a sales dictionary, display it,
    and filter it to show sales greater than 100.
    """
    # Define quarters and prices as lists to preserve order
    quarters = ["A", "B", "C", "D"]
    prices = [100, 200, 300, 400]

    # Combine quarters and prices into a dictionary
    sales = dict(zip(quarters, prices))

    # Display the sales dictionary
    print("Original sales:")
    for quarter, price in sales.items():
        print(f"{quarter}: ${price}")
    print()

    # Filter the sales dictionary
    filter_sales = filtering_sales(sales)
    print("Filtered sales:")
    for quarter, price in filter_sales.items():
        print(f"{quarter}: ${price}")
    print()

    # Apply a 10% tax to the sales
    taxed_sales = taxing_sales(sales)
    print("Sales after tax:")
    for quarter, price in taxed_sales.items():
        print(f"{quarter}: ${price}")


if __name__ == "__main__":
    main()
