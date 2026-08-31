"""Functions to help play and score a game of blackjack.
 
How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""
def value_of_card(card):
    """Determine the scoring value of a card."""
    face_cards = ['J', 'Q', 'K']
    if card in face_cards:
        return 10
    if card == 'A':
        return 1
    return int(card)
def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand."""
    one_value = value_of_card(card_one)
    two_value = value_of_card(card_two)
    if one_value > two_value:
        return card_one
    if one_value == two_value:
        return card_one, card_two
    return card_two
def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for an upcoming ace card."""
    one_value = value_of_card(card_one)
    two_value = value_of_card(card_two)    
    if one_value == 1 or two_value == 1 or one_value + two_value + 11 > 21:
        return 1
    return 11
def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'."""
    ten_cards = ['10', 'K', 'Q', 'J']
    if card_one in ten_cards:
        if card_two == 'A':
            return True
    elif card_two in ten_cards:
        if card_one == 'A':
            return True
    return False
def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands."""
    one_value = value_of_card(card_one)
    two_value = value_of_card(card_two)
    if one_value == two_value:
        return True
    return False
def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet."""
    one_value = value_of_card(card_one)
    two_value = value_of_card(card_two)
    total = one_value + two_value
    doub_down = [9, 10, 11]
    if total in doub_down:
        return True
    return False
