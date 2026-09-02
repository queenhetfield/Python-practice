"""Module providing a function translating English into Pig Latin."""
def translate(text):
    """Function translating English into Pig Latin."""
    words = text.split()
    vowels = ["a", "e", "i", "o", "u"]
    new_words = []

    for word in words:
        cons = ""
        split_index = 0
        remaining_word = word

        if word[0] in vowels or word[:2] == "xr" or word[:2] == "yt":
            new_word = word + "ay"
        else:
            while word[split_index] not in vowels and word[split_index:split_index+2] != "qu":
                split_index += 1
                cons = word[:split_index]
                remaining_word = word[split_index:]
                if remaining_word[0] == "y" and cons != "":
                    break

        if remaining_word[:2] == "qu":
            new_word = remaining_word[2:] + cons + "qu" + "ay"

        elif remaining_word[0] == "y":
            new_word = "y" + remaining_word[1:] + cons + "ay"
        else:
            new_word = remaining_word + cons + "ay"      

        new_words.append(new_word)
    return " ".join(new_words)

if __name__ == "__main__":
    print(translate("chair"))