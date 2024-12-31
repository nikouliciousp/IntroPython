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

# Print with custom end
print("This is the first line.", end=" ")
print("This is on the same line because of 'end'.")

# Multi-line print using triple quotes
print("""This is a 
multi-line 
string print.""")

# Print output to a file
with open("output.txt", "w") as file:
    print("This is written to a file.", file=file)