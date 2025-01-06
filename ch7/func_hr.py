def sqr(x):
    # Function to calculate the square of a number
    return x ** 2


def cube(x):
    # Function to calculate the cube of a number
    return x ** 3


def my_func(func, nums):
    # Apply the given function (func) to each element in the list (nums)
    return [func(num) for num in nums]


def main():
    # List of numbers
    nums = [1, 2, 3, 4, 5]
    # Print the squares of the numbers
    print(f"Squares: {my_func(sqr, nums)}")
    # Print the cubes of the numbers
    print(f"Cubes: {my_func(cube, nums)}")


if __name__ == "__main__":
    # Execute the main function if the script is run directly
    main()
