class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """Adds an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Removes and returns the top item from the stack. Raises error if the stack is empty."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        """Returns the top item of the stack without removing it. Raises error if the stack is empty."""
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def is_empty(self):
        """Checks if the stack is empty."""
        return len(self.items) == 0

    def size(self):
        """Returns the size of the stack."""
        return len(self.items)

def main():
    """
    Main function to handle user input choices and call the stack methods.
    """
    stack = Stack()
    while True:
        print("\nMenu:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Check if empty")
        print("5. Stack size")
        print("6. View stack contents")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        try:
            if choice == '1':
                item = input("Enter item to push: ")
                stack.push(item)
                print(f"Item '{item}' pushed to stack.")
            elif choice == '2':
                popped_item = stack.pop()
                print(f"Popped item: {popped_item}")
            elif choice == '3':
                top_item = stack.peek()
                print(f"Top item: {top_item}")
            elif choice == '4':
                print("Stack is empty." if stack.is_empty() else "Stack is not empty.")
            elif choice == '5':
                print(f"Stack size: {stack.size()}")
            elif choice == '6':
                print(f"Stack contents: {stack.items}")
            elif choice == '7':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 7 without spaces.")
        except IndexError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    print("Stack")
    print(main.__doc__)
    main()