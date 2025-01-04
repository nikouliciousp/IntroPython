import math

class Circle:
    def __init__(self, radius: float = 0.0):
        """
        Represents a circle with a defined radius.

        Attributes
        __radius : float
            The radius of the circle, default is 0.0.

        Parameters
        radius : float, optional
            The radius of the circle. Defaults to 0.0.

        """
        self.__radius = radius

    @property
    def radius(self):
        """
        Gets the radius value of a circle.

        This property fetches the private attribute `__radius` and provides
        read-only access to its value. It ensures encapsulation by not
        allowing direct modification of the private attribute.

        :raises AttributeError: if an attempt to set this property is made.
        :return: The radius value of the circle.
        :rtype: float
        """
        return self.__radius

    @radius.setter
    def radius(self, value):
        """
        Sets the radius of a circle, ensuring that it does not take negative values.

        This setter method allows the user to set a new value for the radius while
        enforcing that only non-negative values are permissible. If a negative value is
        provided, a ValueError is raised.

        :param value: The new value for the circle's radius, which must be non-negative.
        :type value: float
        :raises ValueError: If the provided value is negative.
        """
        if value < 0:
            raise ValueError("Radius cannot be negative.")
        self.__radius = value

    @property
    def calculate_circumference(self):
        """
        Calculate the circumference of a circle.

        This method calculates the circumference of the circle using the formula:
        2 * π * radius, where π is mathematical constant pi. The radius is an internal
        property of the class.

        :return: The circumference of the circle.
        :rtype: float
        """
        return 2 * math.pi * self.__radius

    @property
    def calculate_area(self):
        """
        Calculate the area of a circle given its radius.

        This function computes the area of a circle using the mathematical formula:
        area = π * radius^2. The radius of the circle is accessed as a private
        attribute of the class.

        :return: The calculated area of the circle
        :rtype: float
        """
        return math.pi * self.__radius ** 2

    def display_info(self):
        """
        Displays information about the circle, including its radius, area,
        and circumference. This method encapsulates its functionality by
        accessing private attributes and invoking corresponding calculation
        methods for displaying computed values.
        """
        print(f"Radius: {self.__radius}")
        print(f"Area of circle: {self.calculate_area}")
        print(f"Circumference of circle: {self.calculate_circumference}")

def main():
    """
    Main function to test the Circle class.
    """
    circle = Circle(5)
    circle.display_info()
    print()
    circle.radius = 10
    print(f"Radius: {circle.radius}")
    print(f"Area of circle: {circle.calculate_area}")
    print(f"Circumference of circle: {circle.calculate_circumference}")
    del circle

if __name__ == "__main__":
    main()
