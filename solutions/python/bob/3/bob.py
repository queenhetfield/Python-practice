"""Module, that contains function that determines what Bob will reply to someone when
    they say something to him or ask him a question."""
def response(hey_bob):
    """Function that determines Bob's reply."""
    stripped = hey_bob.strip()
    if stripped == "":
        return "Fine. Be that way!"
    if hey_bob.upper() == hey_bob and any(char.isalpha() for char in hey_bob):
        if stripped[-1] == "?":
            return "Calm down, I know what I'm doing!"
        return "Whoa, chill out!"
    if stripped[-1] == "?":
        return "Sure."
    return "Whatever."
