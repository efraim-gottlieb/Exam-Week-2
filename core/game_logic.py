from core.player_io import ask_player_action

def calculate_hand_value(hand: list[dict]) -> int:
    total = 0
    for card in hand:
        if card['rank'] == 'A':
            total += 1
        elif card['rank'] in ['J', 'Q', 'K']:
            total += 10
        else:
            total += int(card['rank'])
    return total
    
def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    card_1 = deck.pop()
    card_2 = deck.pop()
    player['hand'].append(card_1)
    dealer['hand'].append(card_2)
    print(f'dealer hand value :{calculate_hand_value(dealer['hand'])}')
    print(f'player hand value :{calculate_hand_value(player['hand'])}')

def dealer_play(deck: list[dict], dealer: dict) -> bool:
    while calculate_hand_value(dealer['hand']) <= 17:
        dealer['hand'].append(deck.pop())
    if calculate_hand_value(dealer['hand']) > 21 :
        print('dialer loss !')
        return False
    return True

def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    deal_two_each(deck, player, dealer)
    game = True
    choice = None
    while game and choice != 'S':
        choice = ask_player_action()
        if choice == 'H':
            player['hand'].append(deck.pop())
            game = calculate_hand_value(player['hand']) <= 21
            print(calculate_hand_value(player['hand']))
            if not game:
                print('dealer won !')
                return
    dealer_round = dealer_play(deck, dealer)
    if dealer_round:
        if calculate_hand_value(dealer['hand']) > calculate_hand_value(player['hand']):
            print('dealer won !')
        elif calculate_hand_value(dealer['hand']) < calculate_hand_value(player['hand']):
            print('player won !')
        else:
            print('draw')
    else:
        print('player won !')
        