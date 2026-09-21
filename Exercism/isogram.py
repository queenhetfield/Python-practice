"""Module providing a function that determines if a word or phrase is an isogram."""

def is_isogram(phrase):
    """Function determines if a word or phrase is an isogram."""
    phrase = "".join(letter.lower() for letter in phrase if letter.isalpha())
    return all(phrase.count(letter) == 1 for letter in phrase)
