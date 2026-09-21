"""Module providing a function that checks if sentence is a pangram."""
from string import ascii_lowercase

alphabet_set = set(ascii_lowercase)
def is_pangram(sentence):
    """Function that checks if sentence is a pangram."""
    return alphabet_set.issubset(sentence.lower())
