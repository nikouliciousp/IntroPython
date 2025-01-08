from point import Point

def main():
    # Create two points
    point1 = Point(3, 4)
    point2 = Point(1.1, 2.3)

    # Print the points
    print(f"Point1: {point1}")
    print(f"Point2: {point2}")

    # Add two points
    try:
        result_add = point1 + point2
        print(f"Addition of Point1 and Point2: {result_add}")
    except Exception as e:
        print(f"Error adding Point1 and Point2: {e}")

    # Subtract two points
    try:
        result_sub = point1 - point2
        print(f"Subtraction of Point1 and Point2: {result_sub}")
    except Exception as e:
        print(f"Error subtracting Point1 and Point2: {e}")

    # Equality check
    try:
        print(f"Are Point1 and Point2 equal? {'Yes' if point1 == point2 else 'No'}")
    except Exception as e:
        print(f"Error checking equality of Point1 and Point2: {e}")

    # Polymorphic function
    def add_points(a, b):
        try:
            return a + b
        except Exception as e:
            print(f"Error in polymorphic function add_points: {e}")
            return None

    result = add_points(point1, point2)
    if result is not None:
        print(f"Addition of Point1 and Point2 using polymorphic function: {result}")

    result = add_points(point1, 2)
    if result is not None:
        print(f"Addition of Point1 and 2 using polymorphic function: {result}")

if __name__ == "__main__":
    main()
