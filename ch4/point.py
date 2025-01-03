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


if __name__ == "__main__":
    main()
