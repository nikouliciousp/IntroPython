class Student:
    """
    A class to represent a student with a name and age.
    """

    def __init__(self, firstname, lastname, age):
        """
        Initialize the student's name and age.

        :param firstname (str): The firstname of the student.
        :param lastname (str): The lastname of the student.
        :param age (int): The age of the student.
        """
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def display_info(self):
        """
        Print the student's name and age.
        """
        print(f"Firstname: {self.firstname}\nLastname: {self.lastname}\nAge: {self.age}")


def main():
    """
    Main function to create a Student object and display its information.
    """
    student = Student("John", "Doe", 20)
    student.display_info()


if __name__ == "__main__":
    main()
