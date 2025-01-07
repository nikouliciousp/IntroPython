def common_member(list1, list2):
    # Find all common elements without duplicates
    return list(set(list1) & set(list2))


def main():
    list1 = [4, 5, 2, 6, 5, 8, 1, 1, 2, 2, 3, 10]
    print(f"List 1: {list1}")
    list2 = [2, 2, 3, 4, 5, 6]
    print(f"List 2: {list2}")

    # Get the list of all common elements without duplicates
    common_list = common_member(list1, list2)
    print(f"Common elements without duplicates: {list(common_list)}")


if __name__ == "__main__":
    main()
