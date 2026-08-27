"""Module providing a function determining if year is a leap year."""
def leap_year(year):
    """Function determining if year is a leap year."""
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False