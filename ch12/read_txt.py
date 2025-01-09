# Function to read content from a file
def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)

read_file('test.txt')
print('Done')