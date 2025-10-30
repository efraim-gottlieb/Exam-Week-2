def build_standard_deck() -> list[dict]:
    deck = []
    for suit in ["H", "C", "D", "S"]:
        for special_rank in ['J', 'Q', 'K', 'A']:
            deck.append({'rank' : special_rank, 'suite' : suit})
        for i in range(2,11):
            deck.append({'rank' : str(i +1), 'suite' : suit})
    return deck

a = build_standard_deck()
for i in a:
    print(i)
print(len(a))


def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    return [{}]
