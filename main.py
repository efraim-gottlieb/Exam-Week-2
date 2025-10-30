from core.deck import build_standard_deck
from core.deck import shuffle_by_suit
from core.game_logic import run_full_game
from core.game_logic import calculate_hand_value

if __name__ == '__main__':
    deck = build_standard_deck()
    shuffle_by_suit(deck)
    player = {"hand": []} 
    dealer = {"hand": []}
    run_full_game(deck, player, dealer)
