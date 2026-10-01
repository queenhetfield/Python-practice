"""Module containing a function, which translates binary seq. into secret handshake."""
def commands(binary_str):
    """Function, which translates binary seq. into secret handshake."""
    handshake = []
    actions = ("wink", "double blink", "close your eyes", "jump")
    for digit, action in zip(binary_str[:0:-1], actions):
        if digit == "1":
            handshake.append(action)
    if binary_str[0] == "1":
        handshake.reverse()
    return handshake
