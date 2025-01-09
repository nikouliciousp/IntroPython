from vehicle import *

def main():
    """
    Main function to demonstrate polymorphism in Vehicle hierarchy and driving vehicles.
    """

    def drive_vehicle(vehicle):
        """
        Function to call the drive method on a given vehicle.

        Args:
            vehicle (Vehicle): An instance of a class derived from Vehicle.
        """
        vehicle.drive()

    # Create a car and a truck instance
    car = Car()
    truck = Truck()

    # Drive both the car and the truck
    drive_vehicle(car)
    drive_vehicle(truck)


if __name__ == "__main__":
    main()