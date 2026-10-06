"""Module providing a function implementing a binary search algorithm."""
def find(search_list, value):
    """Function implementing a binary search algorithm."""
    chopping_list = search_list
    while len(chopping_list) > 1:
        middle = len(chopping_list) // 2
        if chopping_list[middle] == value:
            return search_list.index(value)
        if chopping_list[middle] > value:
            chopping_list = chopping_list[:middle]
        else:
            chopping_list = chopping_list[middle:]
    if search_list and search_list[0] == value:
        return search_list.index(value)
    raise ValueError("value not in array")
