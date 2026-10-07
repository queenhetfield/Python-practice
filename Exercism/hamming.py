"""Module providing a function calculating the Hamming distance between two DNA strands."""
def distance(strand_a, strand_b):
    """Function returns calcualted Hamming distance between two DNA strands."""
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")

    hamming_distance = 0
    for char_a, char_b in zip(strand_a, strand_b):
        if char_a != char_b:
            hamming_distance += 1
    return hamming_distance
