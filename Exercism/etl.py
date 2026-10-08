"""Module containing function which converts the data format of letters and their point values in the game."""
def transform(legacy_data):
    """Function returns converted data in dict."""
    letters = []
    for value in legacy_data.values():
        letters.extend(value)
    transformed = {}
    for letter in sorted(letters):
        transformed[letter.lower()] = next(key for key, value in legacy_data.items() if letter in value)
    return transformed
