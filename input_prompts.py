"""Input tree for gathering poker data"""

import sys
from data_parser import extract_players, add_player_results, add_new_player, add_date


def startup_prompt():
    """Find out what user wants to do upon opening program"""

    option = input('Type "start" to enter new poker data, "view" to see the current chart, or "quit" to quit.\n')

    if option == 'quit':
        sys.exit()
    elif option == 'view':
        import visual
        startup_prompt()
    elif option == 'start':
        new_players_prompt()
    else:
        startup_prompt()


def date_prompt():
    """Get the date for the current poker session"""

    date = input("Enter today's date (m/d): ")

    date_confirm = input(f"Today is {date}. Is this correct? (y/n): ")

    if date_confirm != 'y':
        date_prompt()
    else:
        # Add date to database, then ask about new players
        add_date(date)
        print("Date saved.")
        confirm_players_prompt()


def new_players_prompt():
    """Inquire about possible new players and redirect accordingly"""

    new_player_confirm = input("Are there new players today? (y/n): ")

    if new_player_confirm == 'y':
        add_new_player_prompt()
    elif new_player_confirm == 'n':
        date_prompt()
    else:
        new_players_prompt()


def confirm_winnings_prompt(players):
    """Takes in standings after the game and adds to the database"""

    # Asks for each players new standing and stores in score_update
    score_update = {}

    for player in players:
        result = input(f"End result for {player.title()}?: ")
        score_update[player] = result

    # Confirms standings saves to database
    save_confirm = input('Please review final results. Save and view graph? (y/n)')
    if save_confirm == 'y':
        add_player_results(score_update)
        import visual
        sys.exit()
    else:
        confirm_winnings_prompt(players)


def confirm_players_prompt():
    """Asks if all registered players are playing."""

    # Shows all registered players
    players = [player for player, scores in extract_players('player_data.txt').items()]

    print("\nHere's the current poker roster.")

    for player in players:
        print(player.title())

    # If there are missing players, take them out of this session
    all_players_confirm = input("Is everyone playing today? (y/n): ")

    if all_players_confirm == 'y':
        confirm_winnings_prompt(players)
    elif all_players_confirm == 'n':
        remove_missing_players_prompt(players)


def remove_missing_players_prompt(players):
    """Removes players who aren't playing today and retains score for missing players"""

    # Asks for missing players, one at a time
    missing_players = []

    print("Who isn't playing? Type in each player's name as it was listed one at a time")
    print("Type 'done' when you're finished.\n")

    player = ""

    while player != 'done':
        player = input("Player: ")

        if player.lower() in players:
            missing_players.append(player.lower())
        elif player not in players:
            print("Can't find that player. Re-enter with no spelling mistakes.")

    # If they 'done' was entered without any players, returns to confirm_players_prompt()
    if not missing_players:
        confirm_players_prompt()
    else:
        # Confirms missing players and retains the current players
        print("These are the missing players.\n")
        for player in missing_players:
            print(player.title())

        missing_player_confirm = input("Is this correct? (y/n): ")

        if missing_player_confirm != 'y':
            remove_missing_players_prompt(players)
        else:
            # Sends a list of the current players to the confirm winnings prompt
            current_players = []
            for player in players:
                if player not in missing_players:
                    current_players.append(player)
            confirm_winnings_prompt(current_players)


def add_new_player_prompt():
    """Asks about new player and adds them to the database"""

    print("What is the new player's name? Must be one word, and must be unique.")
    print("Type 'cancel' to proceed without adding a new player.")

    new_player = input("Player: ")

    if new_player == 'cancel':
        confirm_players_prompt()
    else:
        confirm_player = input(f"New player's name is {new_player}. Is this correct? (y/n): ")

        if confirm_player != 'y':
            add_new_player_prompt()
        else:
            add_new_player(new_player.lower())

            print("Player saved.")

            # Ask if there's any more players to add to the roster
            add_another_player_confirm = input("Is there another player you'd like to add? (y/n): ")

            if add_another_player_confirm != 'y':
                date_prompt()
            else:
                add_new_player_prompt()
