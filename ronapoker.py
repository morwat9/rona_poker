import pyfiglet
from input_prompts import startup_prompt
from data_parser import extract_players

print(pyfiglet.figlet_format("Rona Poker"))

# players = [player for player, scores in extract_players('player_data.txt').items()]

startup_prompt()
