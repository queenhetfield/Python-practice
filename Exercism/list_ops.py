"""Module containing implementation of basic list operations."""
def append(list1, list2):
    """Function appending one list to another."""
    for element in list2:
        list1 += [element]
    return list1


def concat(lists):
    """Function combining all lists in a initial list to return flattened list."""
    flattened = []
    for element in lists:
        if isinstance(element, list):
            flattened.extend(element)
        else:
            flattened.append(element)
    return flattened


def filter(function, list):
    """Function returning filteren list based on input function."""
    return [item for item in list if function(item)]


def length(list):
    """Function returning length of the list."""
    #generator?
    items = 0
    for _ in list:
        items += 1
    return items
    

def map(function, list):
    """Function returning a list with applied funtion on all list items."""
    return [function(item) for item in list]
        

def foldl(function, list, initial):
    """Funtion return left fold."""
    accumulated = initial
    for item in list:
        accumulated = function(accumulated, item)
    return accumulated


def foldr(function, list, initial):
    """Funtion return right fold."""
    accumulated = initial
    for item in list[::-1]:
        accumulated = function(accumulated, item)
    return accumulated


def reverse(list):
    """Funtion returning reversed list."""
    return [element for element in list[::-1]]
