# Basic print statement
print("This is a basic print statement.")

# Print with string concatenation
print("Hello" + ", " + "world!")

# Print using f-strings (formatted strings)
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")

# Print using str.format() with numbered placeholders
print("My name is {0} and I am {1} years old.".format(name, age))

# Print using % formatting
print("My name is %s and I am %d years old." % (name, age))

# Print with custom separator
print("Python", "is", "awesome", sep="-")

# Demonstrating sep argument with different separators
print("Red", "Green", "Blue", sep=", ")
print("1", "2", "3", sep=" -> ")

# Print with custom end
print("This is the first line.", end=" ")
print("This is on the same line because of 'end'.")

# Demonstrating end argument with different endings
print("Line 1", end=" | ")
print("Line 2", end="\n\n")  # Add double newlines

# Multi-line print using triple quotes
print("""This is a 
multi-line 
string print.""")

# Demonstrating flush argument to force immediate output
import time
for i in range(3):
    print(f"Progress: {i + 1}/3", flush=True, end="\r")
    time.sleep(1)
print("Done!", flush=True)

# Print output to a file
with open("output.txt", "w") as file:
    print("This is written to a file.", file=file)

# Demonstrating file argument by writing multiple lines to another file
with open("log.txt", "w") as file:
    print("Log Entry 1: System started.", file=file)
    print("Log Entry 2: System is running.", file=file)

