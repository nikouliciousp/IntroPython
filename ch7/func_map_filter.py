def map_filter(cities):
    # Convert each city name to uppercase
    # Filter only cities with names longer than 5 characters
    return list(filter(lambda city: len(city) > 5, map(lambda city: city.upper(), cities)))


def main():
    # List of city names
    cities = ["London", "Berlin", "Paris", "Rome"]
    # Print the result of applying the map_filter function to the list of cities
    print(f"Cities with names longer than 5 characters: {map_filter(cities)}")


if __name__ == "__main__":
    main()
