"""Module providing a function to find anagrams."""
def find_anagrams(word, candidates):
    """Function finding anagrams."""
    anagrams = []
    for candidate in candidates:
        if sorted(list(candidate.lower())) == sorted(list(word.lower())) and word.lower() != candidate.lower():
            anagrams.append(candidate)
    return anagrams
