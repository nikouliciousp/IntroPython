class Point:
    """
    A class to represent a point in 2D space.

    Attributes:
        x (float or int): The x-coordinate of the point.
        y (float or int): The y-coordinate of the point.
    """

    def __init__(self, x, y):
        """
        Initializes a Point instance.

        Args:
            x (float or int): The x-coordinate of the point.
            y (float or int): The y-coordinate of the point.
        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        Returns a string representation of the point.

        Returns:
            str: A string in the format "(x, y)".
        """
        return f"({self.x:.2f}, {self.y:.2f})"

    def __add__(self, other):
        """
        Adds the current point to another point or a scalar value.

        Args:
            other (Point or float or int): The other operand.

        Returns:
            Point: A new point resulting from the addition.

        Raises:
            TypeError: If the other operand is not a Point, int, or float.
        """
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):
            return Point(self.x + other, self.y + other)
        else:
            raise TypeError(f"Unsupported operand type(s) for +: '{type(self)}' and '{type(other)}'")

    def __sub__(self, other):
        """
        Subtracts another point or a scalar value from the current point.

        Args:
            other (Point or float or int): The other operand.

        Returns:
            Point: A new point resulting from the subtraction.

        Raises:
            TypeError: If the other operand is not a Point, int, or float.
        """
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        elif isinstance(other, (int, float)):
            return Point(self.x - other, self.y - other)
        else:
            raise TypeError(f"Unsupported operand type(s) for -: '{type(self)}' and '{type(other)}'")

    def __radd__(self, other):
        """
        Implements reverse addition for the Point class.

        Args:
            other (Point or float or int): The other operand.

        Returns:
            Point: The result of the addition.
        """
        return self.__add__(other)

    def __rsub__(self, other):
        """
        Implements reverse subtraction for the Point class.

        Args:
            other (Point or float or int): The other operand.

        Returns:
            Point: The result of the subtraction.
        """
        if isinstance(other, (int, float)):
            return Point(other - self.x, other - self.y)
        else:
            raise TypeError(f"Unsupported operand type(s) for -: '{type(other)}' and '{type(self)}'")

    def __eq__(self, other):
        """
        Checks if two points are equal.

        Args:
            other (Point): The other point to compare.

        Returns:
            bool: True if the points have the same coordinates, False otherwise.
        """
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        else:
            return False

    def __hash__(self):
        """
        Returns a hash value for the point.

        Returns:
            int: A hash value based on the point's coordinates.
        """
        return hash((self.x, self.y))