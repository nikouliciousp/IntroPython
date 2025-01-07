def fahrenheit_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    :param fahrenheit: Temperature in Fahrenheit
    :return: Temperature in Celsius
    """
    return (fahrenheit - 32) * 5.0 / 9.0

def celsius_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    :param celsius: Temperature in Celsius
    :return: Temperature in Fahrenheit
    """
    return celsius * 9.0 / 5.0 + 32

def convert_temperature():
    """
    Allows user to choose conversion direction and prints the result.
    """
    choice = input("Type 'F' to convert Fahrenheit to Celsius or 'C' to convert Celsius to Fahrenheit: ").strip().upper()
    if choice == "F":
        fahrenheit = float(input("Enter Fahrenheit temperature: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit:.2f}°F is equivalent to {celsius:.2f}°C")
    elif choice == "C":
        celsius = float(input("Enter Celsius temperature: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius:.2f}°C is equivalent to {fahrenheit:.2f}°F")
    else:
        print("Invalid choice. Please try again.")

def main():
    convert_temperature()

if __name__ == "__main__":
    main()