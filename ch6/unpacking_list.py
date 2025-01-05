def main():
    # Example of slicing in lists
    # Extracting a portion of the list
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    sliced_list = my_list[2:7]  # [3, 4, 5, 6, 7]
    print(sliced_list)

    # Example of extended unpacking in lists
    # Splitting a list into separate parts
    first, *middle, last = my_list  # first=1, middle=[2, 3, 4, 5, 6, 7, 8], last=9
    print(first, middle, last)


if __name__ == "__main__":
    main()
