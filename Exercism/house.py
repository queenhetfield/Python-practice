"""Module providing function that recites nursery rhyme 'This is the House that Jack Built'. """
rhyme = {
1: ("house ", "Jack built."),
2: ("malt ","lay in "),
3: ("rat ", "ate "),
4: ("cat ", "killed "),
5: ("dog ", "worried "),
6: ("cow with the crumpled horn ", "tossed "),
7: ("maiden all forlorn ", "milked "),
8: ("man all tattered and torn ", "kissed "),
9: ("priest all shaven and shorn ", "married "),
10: ("rooster that crowed in the morn ", "woke "),
11: ("farmer sowing his corn ", "kept "),
12: ("horse and the hound and the horn ", "belonged to ")
}


def recite(start_verse, end_verse):
    """Function that recites nursery rhyme 'This is the House that Jack Built'."""
    recited = []
    for verse in range(start_verse, end_verse + 1):
        phrases = ""
        for phrase_number in range(verse, 0, -1):
            phrase = "the "+ rhyme[phrase_number][0] + "that " + rhyme[phrase_number][1]
            phrases += phrase
        recited.append("This is " + phrases)
    return recited

print(recite(5, 6))