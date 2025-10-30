def ask_player_action() -> str: 
    choice = None
    while not choice in ['S', 'H']:
        choice = input("Enter your choice ( 's' or 'h') ")
    return choice

def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    pass

print(ask_player_action())