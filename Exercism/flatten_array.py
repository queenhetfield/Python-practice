"""Module providing a function to unpack inputs."""
def flatten(iterable):
    """Function returning unpacked inputs."""
    unpacked = []
    for element in iterable:
        if element is None:
            continue
        if isinstance(element, list):
            unpacked.extend(flatten(element))
        else:
            unpacked.append(element)
    return unpacked
