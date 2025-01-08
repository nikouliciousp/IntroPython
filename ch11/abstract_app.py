from ch11.store import Item, OutOfStockError


class AbstractStudentDAO:
    """
    Represents an abstract Data Access Object (DAO) for managing student
    entities in a data store. This is a base class that defines the interface 
    for implementing concrete DAO classes. It outlines the required methods 
    for interacting with the data store, such as inserting, updating, deleting, 
    and retrieving a single student entity.

    Methods:
        insert: Abstract method to insert a student entity.
        update: Abstract method to update a student entity.
        delete: Abstract method to delete a student entity.
        getOne: Abstract method to retrieve a student entity.
    """

    def insert(self):
        """
        Abstract method to insert a student entity into the data store.
        Must be implemented in a subclass.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def update(self):
        """
        Abstract method to update an existing student entity in the data store.
        Must be implemented in a subclass.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def delete(self):
        """
        Abstract method to delete a student entity from the data store.
        Must be implemented in a subclass.
        """
        raise NotImplementedError("Subclasses must implement this method.")

    def getOne(self):
        """
        Abstract method to retrieve a single student entity from the data store.
        Must be implemented in a subclass.
        """
        raise NotImplementedError("Subclasses must implement this method.")


class StudentImpl(AbstractStudentDAO):
    """
    Implementation of the AbstractStudentDAO for managing student entities.
    Provides concrete implementations of the required methods.
    """

    def insert(self):
        """
        Inserts a new student entity into the data store.
        Implementation of the abstract method `insert`.
        """
        # TODO: Implement the logic to insert a student into the data store
        pass

    def update(self):
        """
        Updates an existing student entity in the data store.
        Implementation of the abstract method `update`.
        """
        # TODO: Implement the logic to update a student in the data store
        pass

    def delete(self):
        """
        Deletes a student entity from the data store.
        Implementation of the abstract method `delete`.
        """
        # TODO: Implement the logic to delete a student from the data store
        pass

    def getOne(self):
        """
        Retrieves a single student entity from the data store.
        Implementation of the abstract method `getOne`.
        """
        # TODO: Implement the logic to retrieve a student from the data store
        pass


from abc import ABC, abstractmethod


class ABCInventory(ABC):
    """
    Abstract base class (ABC) for inventory management.
    Defines the required methods for managing inventory items.

    Methods:
        insert: Abstract method to insert an item.
        update: Abstract method to update an item.
        delete: Abstract method to delete an item.
        getOne: Abstract method to retrieve an item.
        print_items: Abstract method to print all items in the inventory.
    """

    @abstractmethod
    def insert(self, item):
        pass

    @abstractmethod
    def update(self, item):
        pass

    @abstractmethod
    def delete(self, item):
        pass

    @abstractmethod
    def getOne(self, item):
        pass

    @abstractmethod
    def print_items(self):
        pass


class Inventory(ABCInventory):
    """
    Concrete implementation of the ABCInventory for managing inventory items.

    Attributes:
        items (list): The list of items in the inventory.

    Methods:
        insert: Adds a new item to the inventory.
        update: Updates the quantity or details of an item.
        delete: Decreases the quantity of an item or removes it if out of stock.
        getOne: Retrieves a specific item from the inventory.
        print_items: Prints all items and their quantities.
    """

    def __init__(self):
        self.items = []  # Initialize an empty inventory list

    def insert(self, item):
        """
        Adds a new item to the inventory.

        Args:
            item (Item): The item to be added.
        """
        self.items.append(item)

    def update(self, item):
        """
        Updates the details of an existing item in the inventory.

        Args:
            item (Item): The item to be updated.

        Raises:
            ValueError: If the item is not found in the inventory.
        """
        if item not in self.items:
            raise ValueError(f"Item '{item.name}' is not in the inventory.")

        for i in range(len(self.items)):
            if self.items[i] == item:
                self.items[i] = item
                break

    def delete(self, item):
        """
        Decreases the quantity of an item or removes it from the inventory 
        if out of stock.

        Args:
            item (Item): The item to be deleted.

        Raises:
            ValueError: If the item is not found in the inventory.
            OutOfStockError: If the item is out of stock.
        """
        if item not in self.items:
            raise ValueError(f"Item '{item.name}' is not in the inventory.")

        for i in range(len(self.items)):
            if self.items[i] == item:
                if self.items[i].quantity > 0:
                    self.items[i].quantity -= 1
                    return
                else:
                    raise OutOfStockError(item.name)

    def getOne(self, item):
        """
        Retrieves a specific item from the inventory.

        Args:
            item (Item): The item to retrieve.

        Returns:
            Item: The matching item from the inventory.

        Raises:
            ValueError: If the item is not found in the inventory.
        """
        for i in self.items:
            if i == item:
                return i
        raise ValueError(f"Item '{item.name}' is not in the inventory.")

    def print_items(self):
        """
        Prints all items and their quantities in the inventory.
        """
        for item in self.items:
            print(f"{item.name}: {item.quantity}")
