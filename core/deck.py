from random import randint


def build_standard_deck() -> list[dict]:
    deck = []
    for suit in ["H", "C", "D", "S"]:
        for special_rank in ['J', 'Q', 'K', 'A']:
            deck.append({'rank' : special_rank, 'suit' : suit})
        for i in range(2,11):
            deck.append({'rank' : str(i +1), 'suit' : suit})
    return deck

def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    for _ in range(swaps):
        condition_met = False
        while not condition_met:
            i = randint(0, len(deck) -1)
            suit = deck[i]['suit']
            j = randint(0, len(deck) -1)
            not_equal = i != j
            suit_condition_met = not j % 5 if suit == 'H' else not j % 3 if suit == 'C' else not j % 2 if suit == 'D' else not j % 7 if suit == 'S' else ''
            condition_met = not_equal and suit_condition_met
        deck[i], deck[j] = deck[j], deck[i]
    return deck