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
    else:
        return True
    