def square_set_comprehension(n):
    return {x ** 2 for x in range(n)}

if __name__ == "__main__":
    result = square_set_comprehension(10)
    print(result)