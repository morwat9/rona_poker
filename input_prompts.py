"""Input tree for gathering poker data"""

from data_parser import extract_players, add_player_results


def startup_prompt():
    """Find out what user wants to do upon opening program"""
    option = input('Type "start" to enter new poker data, "view" to see the current chart, or "quit" to quit.\n')

    if option == 'quit':
        quit
    elif option == 'view':
        import visual
        startup_prompt()
    elif option == 'start':
        get_session_info()
    else:
        startup_prompt()


def get_session_info():
    """Gather info about who's playing and the date"""
    date = input("Enter today's date (dd/mm):\n")
    confirm = input(f"Today is {date}. Is this correct? (y/n):\n")
    if confirm != 'y':
        get_session_info()
    else:
        with open('dates.txt', 'a') as file_object:
            file_object.write("," + date)
        print("Date saved.")
        # TODO: Show roster and ask more about who's playing
        # print("\nHere's the current poker roster.")
        # for player in players:
        #     print(player.title())
        # TODO: Are any players missing? Omit from adding new scores or keep their score
        # TODO: Any new players? Add them to player_data.txt
        # TODO: Maybe instead of end result, ask how much they gained or lost then do math to get end result
        # confirm_winnings(players)
        confirm_players()


def confirm_winnings(players):
    score_update_dict = {}
    for player in players:
        result = input(f"End result for {player.title()}?: ")
        score_update_dict[player] = result

    save_confirm = input('Please review final results. Save and view graph? (y/n)')
    if save_confirm == 'y':
        add_player_results(score_update_dict)
    else:
        confirm_winnings(players)

def confirm_players():
    players = [player for player, scores in extract_players('player_data.txt').items()]
    print("\nHere's the current poker roster.")
    for player in players:
        print(player.title())