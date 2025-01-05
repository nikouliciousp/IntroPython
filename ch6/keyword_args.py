# Function to filter products based on provided criteria
def filter_products(products, **kwargs):
    # Use list comprehension to filter products matching all criteria
    result = [
        (brand, price)
        for brand, price in products
        if (kwargs.get("brand") == brand) and (kwargs.get("price") == price)
    ]
    return result


# Main function to execute the program
def main():
    products = [("Macbook", 1000), ("iPhone", 500), ("Laptop", 1500)]
    print("Available products:")
    for brand, price in products:
        print(f"Brand: {brand}, Price: {price}")

    brand = input("Enter the brand to filter by: ")
    try:
        price = int(input("Enter the price to filter by: "))
    except ValueError:
        print("Invalid price entered. Please enter a numeric value.")
        return

    criteria = {"brand": brand, "price": price}

    # Filter and print matching products based on the criteria
    filtered_products = filter_products(products, **criteria)
    if filtered_products:
        print(f"Matching products: {filtered_products}")
    else:
        print("No products match the given criteria.")


# Script entry point
if __name__ == "__main__":
    main()
