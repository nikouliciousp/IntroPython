# Example 1: Using a for-in loop to traverse the string
string = "example"
for char in string:
    print(char)

# Example 2: Using a while loop to traverse the string by index
index = 0
while index < len(string):
    print(string[index])
    index += 1

# Example 3: Using list comprehension to create a list of characters
char_list = [char for char in string]
print(char_list)

# Example 4: Using enumerate to iterate over the string with index and character
for index, char in enumerate(string):
    print(f"Index: {index}, Character: {char}")

# Example 5: Using range to traverse the string by index
for i in range(len(string)):
    print(f"Index: {i}, Character: {string[i]}")
