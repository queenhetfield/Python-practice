"""Calculate the number of grains of wheat on a chessboard."""
def square(number):
    if not number in range(65):
        raise ValueError("square must be between 1 and 64")
    if number == 0:
        raise ValueError("square must be between 1 and 64")
    x = 1
    if number == x:
        return x
    elif number > x:
        for i in range (number - 1):
            x *= 2
        return x
def total():
    x = 1
    sum = 1
    for i in range (63):
        x *= 2
        sum = sum + x
    return sum
