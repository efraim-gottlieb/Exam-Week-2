from core.deck import build_standard_deck
from core.deck import shuffle_by_suit
# from core.game_logic import run_full_game
from core.game_logic import deal_two_each

if __name__ == '__main__':
    deck = build_standard_deck()
    shuffle_by_suit(deck)
    print(deck)
    player = {"hand": []} 
    dealer = {"hand": []}
    deal_two_each(deck, player, dealer)
    # run_full_game(deck, player, dealer)