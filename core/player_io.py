def ask_player_action() -> str: 
    choice = None
    while not choice in ['S', 'H']:
        choice = input("Enter your choice ( 'S' or 'H') ")
    return choice.upper()