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
    pass

def dealer_play(deck: list[dict], dealer: dict) -> bool:
    return bool