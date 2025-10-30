from core.deck import build_standard_deck
from core.deck import shuffle_by_suit
# from core.game_logic import run_full_game
from core.game_logic import dealer_play

if __name__ == '__main__':
    deck = build_standard_deck()
    shuffle_by_suit(deck)
    player = {"hand": []} 
    dealer = {"hand": []}
    dealer_play(deck, dealer)


    # run_full_game(deck, player, dealer)