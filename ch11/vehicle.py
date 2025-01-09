class Vehicle:
    """
    Base class to represent a generic vehicle.
    """

    def drive(self):
        """
        Placeholder method to simulate driving a vehicle.
        """
        pass


class Car(Vehicle):
    """
    Class to represent a car, inherited from Vehicle.
    """

    def drive(self):
        """
        Override the drive method to simulate driving a car.
        """
        print("Driving car...")


class Truck(Vehicle):
    """
    Class to represent a truck, inherited from Vehicle.
    """

    def drive(self):
        """
        Override the drive method to simulate driving a truck.
        """
        print("Driving truck...")



