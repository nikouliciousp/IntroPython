def movies(movies_list):
    for i in range(3):
        movie_name = input("Enter movie name: ")
        movie_year = int(input("Enter movie year: "))
        movies_list.append((movie_name, movie_year))

def print_movies(movies_list):
    for movie in movies_list:
        print(f"{movie[0]} was released in {movie[1]}.")

def main():
    movies_list = []
    movies(movies_list)
    print_movies(movies_list)

if __name__ == "__main__":
    main()

