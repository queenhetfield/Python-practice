"""Module contains a function that calculates the points scored in a single toss of a Darts game."""
import math
def score(x, y):
    """Function calculates the points scored in a single toss of a Darts game."""
    distance = math.sqrt(x ** 2 + y ** 2)
    if distance <= 1:
        return 10
    if distance <= 5:
        return 5
    if distance <= 10:
        return 1
    return 0
