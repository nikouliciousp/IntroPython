from collections import deque


class Garage:
    def __init__(self):
        # Initialize a deque to hold cars in the garage
        # deque (double-ended queue) provides fast O(1) append and pop operations
        # from both ends, making it an efficient choice for FIFO or LIFO implementation.
        self.cars = deque()

    def add_car(self, car):
        # Add a car to the garage
        # deque.append() adds an element to the end of the deque efficiently
        self.cars.append(car)
        print(f"Car added: {car}")

    def remove_car(self):
        # Remove a car from the garage, if there are any
        if self.cars:
            # deque.popleft() removes an element from the start of the deque efficiently,
            # making deque well-suited for FIFO (First In, First Out) operations
            removed_car = self.cars.popleft()
            print(f"Car removed: {removed_car}")
            return removed_car
        else:
            print("No cars in the garage!")  # Print a message if the garage is empty
            return None

    def show_garage(self):
        # Display all cars currently in the garage
        print("Cars in garage:", list(self.cars))


def main():
    # Create an instance of the Garage
    garage = Garage()
    garage.add_car("Toyota")  # Add a Toyota to the garage
    garage.add_car("BMW")  # Add a BMW to the garage
    garage.add_car("Ford")  # Add a Ford to the garage
    garage.show_garage()
    garage.remove_car()  # Remove the first car (FIFO)
    garage.show_garage()
    garage.remove_car()  # Remove the next car (FIFO)
    garage.show_garage()  # Display all remaining cars


if __name__ == "__main__":
    # Entry point of the program
    main()

