def main():
    # Example of generator expression: generate squares of numbers from 0 to 9
    squares = (x ** 2 for x in range(10))  # Using generator expression for memory efficiency
    print(f"Type of squares: {type(squares)}")  # Display type of generator object

    # Iterate through the generator and print each square
    print("Squares of numbers from 0 to 9:", end=" ")
    for i in squares:
        print(i, end=" ")


if __name__ == "__main__":
    main()
