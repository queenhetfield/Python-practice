"""Module contains function that converts a number into its corresponding raindrop sounds."""
def convert(number):
    """Function that converts a number into its corresponding raindrop sounds."""
    div_3 = number % 3 == 0
    div_5 = number % 5 == 0
    div_7 = number % 7 == 0

    result = ""
    if div_3:
        result += "Pling"
    if div_5:
        result += "Plang"
    if div_7:
        result += "Plong"
    if result == "":
        result = str(number)
    return result
    