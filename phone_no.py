""" Function to show all possible letter combinations
from telephone digits
"""
import string

def dig_to_letter(d):
    out = []
    d = list(str(d))

    #Create a dictionary of which digits represent which numbers
    digit_letters = {}
    alphabet = list(string.ascii_lowercase)

    batch_size = 3
    digit = 2
    for letters in range(0, len(alphabet), batch_size):
        if digit == 7:
            batch_size = 4
        elif digit == 8:
            batch_size = 3
            letters += 1
        elif digit == 9:
            batch_size = 4
            letters += 1
        batch = alphabet[letters:letters+batch_size]

        digit_letters[str(digit)] = batch
        digit += 1

        if digit == 10:
            break

    #Raising error if input is not allowed
    for digit in d:
        if digit not in digit_letters.keys():
            raise ValueError("Digits must be from 2 to 9")
        
    #Helper function to combine letters
    def _combiner(out, letters):
        if out:
            previous_list = out.copy()
            out.clear()
            for i in previous_list:
                for j in letters:
                    x = str(i + j)
                    out.append(x)
        else:
            for i in letters:
                out.append(i)
        return out
        
    for digit in d:
        letters = digit_letters[digit]
        _combiner(out, letters)

    return out

    
if __name__ == "__main__":
    d = input("Please enter digit(s):\n")
    dig_to_letter(d)
    print(dig_to_letter(8792))

