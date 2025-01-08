import store

def main():
    # Initialize the inventory
    inventory = store.Inventory()

    # Add items to the inventory
    inventory.add_item(store.Item('T-shirt', 10))
    inventory.add_item(store.Item('Pants', 16))
    inventory.add_item(store.Item('Shirt', 10))
    inventory.add_item(store.Item('Hat', 5))

    # Print all items in the inventory
    print("Items in inventory:")
    inventory.print_items()
    print()

    # Try removing an item
    try:
        print("Removing 'Shirt' from inventory:")
        inventory.remove_item('Shirt')
    except (store.OutOfStockError, ValueError) as e:
        print(e)
    finally:
        print("Items in inventory after removal:")
        inventory.print_items()
        print()

    # Print items again to confirm removal
    print("Items in inventory after removal:")
    inventory.print_items()
    print()

    # Additional example - removing a non-existent item
    try:
        print("Attempting to remove 'Socks' (not in inventory):")
        inventory.remove_item('Socks')
    except (store.OutOfStockError, ValueError) as e:
        print(e)
    finally:
        print("Items in inventory after removal:")
        inventory.print_items()

if __name__ == "__main__":
    main()
