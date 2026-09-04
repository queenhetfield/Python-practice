"""Functions for creating, transforming, and adding prefixes to strings."""
import re

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
    """Remove the suffix from the word while keeping spelling in mind."""
    removed = re.sub("ness"," ", word).strip()
    cond = removed[-1:]
    if cond == "i":
        removed = removed.replace("i", "y")
    return removed.strip()
    
def adjective_to_verb(sentence, index):
    """Change the adjective within the sentence to a verb."""
    sentence_list = sentence.split()
    converted = sentence_list[index].strip(".") + "en"
    return converted

if __name__ == "__main__":
    print(remove_suffix_ness("happiness"))

