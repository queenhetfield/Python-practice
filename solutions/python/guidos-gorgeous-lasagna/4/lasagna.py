"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time



def preparation_time_in_minutes(layers_of_lasagna):

    """Calculate the bake time of all layers.

    :param layers_of_lasagna: int - how many layers we are baking.
    :return: int - all layers bake time (in minutes) derived from 'preparation_time_in_minutes'.

    Function that takes the number of layers as
    an argument and returns how many minutes the lasagna needs to bake
    based on the `PREPARATION_TIME`.
    """    
    return PREPARATION_TIME * layers_of_lasagna

def elapsed_time_in_minutes(prepare, bake_time):
    """Calculate the bake time remaining.

    :param elapsed_time_in_minutes: int1 - how many layers we are baking, int2 - how long does it take to bake.
    :return: int - remaining bake time (in minutes).

    Function that takes the number of layers and remaining baking time as
    an argument and returns how many minutes the lasagna still needs to bake
    based.
    """
    return prepare * 2 + bake_time
print(bake_time_remaining.__doc__)
