class OutOfStockError(Exception):
    """Exception raised when an item is out of stock."""

    def __init__(self, item_name):
        """
        Initialize the exception with the name of the item that is out of stock.

        :param item_name: Name of the item that is out of stock.
        """
        super().__init__(f"{item_name} is out of stock.")


class Item:
    """Class representing an item with a name and quantity."""

    def __init__(self, name, quantity):
        """
        Initialize an item with a name and quantity.

        :param name: Name of the item.
        :param quantity: Quantity of the item.
        """
        self.name = name
        self.quantity = quantity

    def __str__(self):
        """
        Return a string representation of the item.

        :return: A string in the format 'name: quantity'.
        """
        return f"{self.name}: {self.quantity}"

    def __eq__(self, other):
        """
        Check if two items are equal based on their names.

        :param other: The other item to compare.
        :return: True if the items have the same name, False otherwise.
        """
        if not isinstance(other, Item):
            return False
        return self.name == other.name

    def __hash__(self):
        """
        Return a hash value for the item based on its name.

        :return: Hash value of the item's name.
        """
        return hash(self.name)


class Inventory:
    """Class representing an inventory to manage items."""

    def __init__(self):
        """Initialize the inventory with an empty list of items."""
        self.items = []

    def add_item(self, item):
        """
        Add a new item to the inventory.

        :param item: The item to add.
        """
        self.items.append(item)

    def remove_item(self, item_name):
        """
        Remove an item from the inventory. Decrease the quantity or remove it completely if the quantity reaches zero.

        :param item_name: The name of the item to remove.
        :return: The updated Item object after decreasing its quantity.
        :raises ValueError: If the item is not found in the inventory.
        :raises OutOfStockError: If the item is out of stock.
        """
        # Check if the item exists in the inventory
        if Item(item_name, None) not in self.items:
            raise ValueError(f"Item '{item_name}' is not in the inventory.")

        # Iterate through the items to find and update the respective item
        for item in self.items:
            if item.name == item_name:
                if item.quantity > 0:
                    item.quantity -= 1
                    return Item(item.name, item.quantity)
                else:
                    raise OutOfStockError(item.name)

    def print_items(self):
        """
        Print all items in the inventory.

        :return: None
        """
        for item in self.items:
            print(item)
