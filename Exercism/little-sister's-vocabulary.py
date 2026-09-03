"""Functions for creating, transforming, and adding prefixes to strings."""

def add_prefix_un(word):
    """Take the given word and add the 'un' prefix."""
    prefixed = "un" + word
    return prefixed

def make_word_groups(vocab_words):
    """Transform a list containing a prefix and words."""
    prefix = vocab_words[0]
    words = vocab_words[1:]
    group = [prefix]
    for word in words:
        prefixed = prefix + word
        group.append(prefixed)
    grouped = " :: ".join(group)
    return grouped

def remove_suffix_ness(word):
    """Remove the suffix from the word while keeping spelling in mind.

    Parameters:
        word (str): Word to remove suffix from.

    Returns:
        str: Word with suffix removed & spelling adjusted.

    Examples:
        >>> remove_suffix_ness('heaviness')
        'heavy'

        >>> remove_suffix_ness('sadness')
        'sad'

    """

    pass


def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb."""
    sentence_list = sentence.split()
    converted = sentence_list[index].strip(".") + "en"
    return converted
