class Point:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        """
        Initialize a Point object with x and y coordinates.

        Args:
            x (float): The x-coordinate of the point. Default is 0.0.
            y (float): The y-coordinate of the point. Default is 0.0.
        
        Attributes:
            __x (float): Private attribute to store the x-coordinate of the point.
            __y (float): Private attribute to store the y-coordinate of the point.
        """
        self.__x = x
        self.__y = y

    @property
    def x(self):
        """Get the x-coordinate of the Point."""
        return self.__x

    @x.setter
    def x(self, value: float):
        """Set the x-coordinate of the Point."""
        self.__x = value

    @property
    def y(self):
        """Get the y-coordinate of the Point."""
        return self.__y

    @y.setter
    def y(self, value: float):
        """Set the y-coordinate of the Point."""
        self.__y = value

    def display_info(self):
        """
        Return a string representation of the Point object.

        Returns:
            str: String representation in the format 'Point(x, y)'.
            
        Attributes:
            __x (float): Private attribute representing the x-coordinate of the point.
            __y (float): Private attribute representing the y-coordinate of the point.
        """
        print(f"Point({self.__x}, {self.__y})")


def main():
    """
    Main function to create a Point object and display its information.
    """
    point = Point(3.2, 2)
    point.display_info()
    point.x = 5.6
    point.y = 7.8
    point.display_info()
    print(point.x)
    print(point.y)


if __name__ == "__main__":
    main()
