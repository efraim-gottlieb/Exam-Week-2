from core.deck import build_standard_deck
from core.deck import shuffle_by_suit


if __name__ == '__main__':
    deck = shuffle_by_suit(build_standard_deck())
    print(deck)