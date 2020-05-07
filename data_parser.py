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


def add_player_results(new_results):
    """Open .txt file and update scores"""

    # Open file and get contents
    with open('player_data.txt') as file_object:
        lines = file_object.readlines()

    # Make a copy of contents, update copy and rewrite entire file
    lines_new = []
    for k, v in new_results.items():
        for line in lines:
            if k in line:
                lines_new.append(line.strip() + f',{v}' + '\n')

    with open('player_data.txt', 'w') as file_object:
        file_object.writelines(lines_new)

    import visual
