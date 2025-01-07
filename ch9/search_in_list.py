# Search with: in, index(), count
def search_in_list_with_in(list_to_search, item_to_search):
    # Check if the item exists in the list using the 'in' keyword
    return item_to_search in list_to_search


def search_in_list_with_index(list_to_search, item_to_search):
    try:
        # Attempt to find the index of the item; if successful, return the index
        return list_to_search.index(item_to_search)
    except ValueError:
        # If ValueError is raised, the item is not in the list
        return None


def search_in_list_with_count(list_to_search, item_to_search):
    # Return the count of occurrences of the item in the list
    return list_to_search.count(item_to_search)


def main():
    list_to_search = [1, 2, 3, 4, 5, 6, 3, 8, 9, 10]
    item_to_search = 3

    # Searching using the 'in' keyword
    print(f"Searching for {item_to_search} in {list_to_search} with 'in':")
    print(search_in_list_with_in(list_to_search, item_to_search))

    # Searching using the index() method
    index_result = search_in_list_with_index(list_to_search, item_to_search)
    if index_result is None:
        print(f"{item_to_search} is not in the list.")
    else:
        print(f"Searching for {item_to_search} in {list_to_search} with 'index()':")
        print(f"The item is at index {index_result}.")

    # Searching using the count() method
    print(f"Searching for {item_to_search} in {list_to_search} with 'count()':")
    print(f"The item occurs {search_in_list_with_count(list_to_search, item_to_search)} times.")


if __name__ == "__main__":
    main()
