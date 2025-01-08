def main():
    # Example of tuple comprehension (using generator expression for tuples)
    numbers = (x * 2 for x in range(5))  # Tuple comprehension-like generator
    for num in numbers:
        print(num)

if __name__ == "__main__":
    main()