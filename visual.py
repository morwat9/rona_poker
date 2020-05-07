"""Matplotlib visuals for graphing winnings over time"""
# TODO: Instead of having 0's when before they started, start their graph when they started
import matplotlib.pyplot as plt
from data_parser import extract_players, extract_dates

player_scores = extract_players('player_data.txt')
dates = extract_dates('dates.txt')

fig, ax = plt.subplots(figsize=(15, 7))
for k, v in player_scores.items():
    ax.plot(v, label=k.title())

plt.legend()
plt.xticks(range(0, len(dates)), dates)
plt.savefig('results.png')
plt.show()

