def main():
    squares_of_even_numbers = [x**2 for x in range(11) if x % 2 == 0]
    print(squares_of_even_numbers)

if __name__ == "__main__":
    main()
