"""Module providing a function implementing Caeser cipher"""
from string import ascii_lowercase, ascii_uppercase

def rotate(text, key):
    """Function implementing Caeser cipher"""
    lowered_text = list(text.lower())
    text = list(text)
    for index, char in enumerate(lowered_text):
        if char in ascii_lowercase:
            rot = ascii_lowercase.index(char) + key
            if rot >= 26:
                rot -=26
            if text[index].islower():
                text[index] = ascii_lowercase[rot]
            else:
                text[index] = ascii_uppercase[rot]
    return "".join(text)
