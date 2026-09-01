def translate(text):

    words = text.split()
    vowels = ["a", "e", "i", "o", "u"]
    new_words = []
    for word in words:
        i = 0
        cons = ""
        remaining_word = word

        while word[i] not in vowels and word[i:i+2] != "qu":
                print(word[i:i+2])
                cons += word[i]
                remaining_word = remaining_word.replace(word[i], "")
                i += 1
                print(remaining_word)

        if remaining_word[:2] == "qu":
            new_word = remaining_word[2:] + cons + "qu" + "ay"
            new_words.append(new_word)
            return " ".join(new_words)

        if word[0] in vowels or word[:2] == "xr" or word[:2] == "yt":
            new_word = word + "ay"
            new_words.append(new_word)
            return " ".join(new_words)
                
        if remaining_word[0] == "y":
            y_index = word.find("y")
            cons = word[:y_index + 1]
            new_word = "y" + cons + word[y_index:]
            new_words.append(new_word)
        else:
            new_word = remaining_word + cons + "ay"
            new_words.append(new_word)
        return " ".join(new_words)

if __name__ == "__main__":
    print(translate("square"))