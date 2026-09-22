"""Module providing a function to check if the provided string is a valid ISBN-10."""
def is_valid(isbn):
    """Function checks if the provided string is a valid ISBN-10."""
    isbn = isbn.replace("-", "")
    if len(isbn) != 10 or not isbn[:-1].isdigit() or (not isbn[-1].isdigit() and isbn[-1] != "X"):
        return False
    isbn_chars = list(isbn)
    if isbn_chars[-1] == "X":
        isbn_chars[-1] = 10

    summed = 0
    multiplier = 10
    for char in isbn_chars:
        summed += (int(char) * (multiplier))
        multiplier -= 1
    return summed % 11 == 0
