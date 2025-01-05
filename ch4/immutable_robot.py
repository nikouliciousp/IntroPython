class ImmutableRobot:

    """
    A counter to keep track of the number of instances created.
    """
    __counter = 0

    """
    A class representing an immutable robot with a name and brand.

    Attributes:
        name (str): The name of the robot.
        brandname (str): The brand of the robot.
    """

    def __init__(self, name, brandname):
        """
        Represents an immutable robot with attributes name and brandname. The class
        also maintains a count of instances created.

        This class is specifically designed to keep the attributes immutable after
        creation, and therefore the values for `name` and `brandname` cannot be
        changed once the instance is created.

        :param name: Represents the name of the robot.
        :param brandname: Represents the brand or manufacturer name of the robot.
        """
        self.__name = name
        self.__brandname = brandname
        ImmutableRobot.__counter += 1

    @property
    def name(self):
        """
        The name property (read-only).

        Returns:
            str: The name of the robot.
        """
        return self.__name

    @property
    def brandname(self):
        """
        The brandname property (read-only).

        Returns:
            str: The brand name of the robot.
        """
        return self.__brandname

    @classmethod
    def count_instances(cls):
        return cls.__counter


def main():
    robot1 = ImmutableRobot(name="RoboX", brandname="TechBot")
    robot2 = ImmutableRobot(name="RoboY", brandname="TechBot")

    print(robot1.name)
    print(robot1.brandname)
    print()
    print(robot2.name)
    print(robot2.brandname)
    print()
    print(f"Total instances created: {ImmutableRobot.count_instances()}")
    print()

    try:
        robot1.name = "RoboY"
    except AttributeError as e:
        print(e)

    try:
        robot1.brandname = "NewTechBot"
    except AttributeError as e:
        print(e)


if __name__ == "__main__":
    main()
