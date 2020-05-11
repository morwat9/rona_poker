"""This module writes and reads data to and from .txt documents"""


def extract_players(player_file):
    """Extracts players and scores, then returns converted data"""

    player_data = {}

    with open(player_file) as file_object:
        for line in file_object:
            # Captures player name
            player = line.rstrip().split(':').pop(0)

            # Captures player scores in a list
            scores_list = line.rstrip().split(':').pop().split(',')

            # Converts str scores to ints and fills dictionary
            player_data[player] = list(map(int, scores_list))

        return player_data


def extract_dates(date_file):
    """Extracts dates and returns a list of them"""

    return open(date_file).readline().split(',')


def add_date(date):
    """Adds the date of the current session to the date file"""

    with open('dates.txt', 'a') as file_object:
        file_object.write("," + date)


def add_player_results(new_results):
    """Open .txt file and update scores"""

    # Open file and get contents
    with open('player_data.txt') as file_object:
        lines = file_object.readlines()

    # Make a copy of contents, update copy and rewrite entire file
    lines_new = []

    for line in lines:
        # If player played, update their score with incoming data
        for k, v in new_results.items():
            if k in line:
                lines_new.append(line.strip() + f',{v}' + '\n')

        # If player didn't play, last score is repeated
        if line.split(':').pop(0) not in new_results:
            last_score = line.split(',').pop()
            lines_new.append(line.strip() + f',{last_score}')

    lines_new.sort()

    with open('player_data.txt', 'w') as file_object:
        file_object.writelines(lines_new)


def add_new_player(new_player):
    """Add a new player to database and start during this date"""

    # Open file and get contents
    with open('player_data.txt') as file_object:
        lines = file_object.readlines()

    # Get the number of games played
    game_count = len(lines.copy().pop().split(','))

    # Create new copy of data
    lines_new = []
    for line in lines:
        lines_new.append(line)

    # Create formatted line for new player in database
    new_player_line = [new_player + ":"]

    for i in range(game_count):
        new_player_line.append("0,")

    str_line = "".join(new_player_line)
    str_line = str_line[:-1] + '\n'

    lines_new.append(str_line)
    lines_new.sort()

    with open('player_data.txt', 'w') as file_object:
        file_object.writelines(lines_new)