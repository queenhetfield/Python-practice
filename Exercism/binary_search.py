"""Module providing a function implementing a binary search algorithm."""
def find(search_list, value):
    """Function implementing a binary search of a string."""
    low = 0
    high = len(search_list)
    while len(search_list[low:high]) > 1:
        middle = (low + high) // 2
        if search_list[middle] == value:
            return middle
        if search_list[middle] > value:
            high = middle
        else:
            low = middle + 1
    if low < len(search_list) and search_list[low] == value:
        return low
    raise ValueError("value not in array")
