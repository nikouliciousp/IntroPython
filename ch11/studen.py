from abc import ABC, abstractmethod  # Step 1: Import ABC module

# Step 2: Abstract class
class Student(ABC):
    def __init__(self, name: str, age: int, student_id: str):
        self.name = name
        self.age = age
        self.student_id = student_id

    @abstractmethod
    def get_details(self) -> str:
        pass

# Step 3: Concrete implementation
class UndergraduateStudent(Student):
    def __init__(self, name: str, age: int, student_id: str, major: str):
        super().__init__(name, age, student_id)
        self.major = major

    def get_details(self) -> str:
        return f"Name: {self.name}, Age: {self.age}, ID: {self.student_id}, Major: {self.major}"

# Step 4: Demonstration code
student = UndergraduateStudent(name="John Doe", age=20, student_id="U12345", major="Computer Science")
print(student.get_details())
