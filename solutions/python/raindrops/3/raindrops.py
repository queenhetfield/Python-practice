"""Module contains function that converts a number into its corresponding raindrop sounds."""
def convert(number):
    """Function that converts a number into its corresponding raindrop sounds."""
    result = ""
    if number % 3 == 0:
        result += "Pling"
    if number % 5 == 0:
        result += "Plang"
    if number % 7 == 0:
        result += "Plong"
    if result == "":
        result = str(number)
    return result
    