def join_args(separator, *args):
    return separator.join(args)

def main():
    print(join_args('-', 'a', 'b', 'c'))
    print(join_args('|', 'a', 'b', 'c', 'd'))

    day_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    print(join_args(', ', *day_of_week))

if __name__ == "__main__":
    main()