# Parent class
class Animal:
    def sound(self):
        # Polymorphic method
        return "Some generic animal sound"

# Subclass 1
class Dog(Animal):
    def sound(self):
        # Overriding method
        return "Bark"

# Subclass 2
class Cat(Animal):
    def sound(self):
        # Overriding method
        return "Meow"

# Main method to demonstrate polymorphism
def main():
    # Creating instances of different subclasses
    animals = [Dog(), Cat(), Animal()]
    
    # Demonstrating polymorphism
    for animal in animals:
        print(animal.sound())

# Entry point of the script
if __name__ == "__main__":
    main()