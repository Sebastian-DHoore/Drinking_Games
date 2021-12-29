import matplotlib.pyplot as plt

file1 = 'Drinking_game_data/Turns.txt'
file2 = 'Drinking_game_data/Shots.txt'
turns_file = open(file1, 'r')
shots_file = open(file2, 'r')
turns = turns_file.read()
shots = shots_file.read()
turns_list = turns.split(", ")
turns_list.remove("")
shots_list = shots.split(", ")
shots_list.remove("")
turns_list = [int(x) for x in turns_list]
amount_of_games = len(turns_list)
shots_list = [int(x) for x in shots_list]
plt.hist(turns_list, bins=30, label='Turns', alpha=0.5)
plt.hist(shots_list, bins=30, label='Shots', alpha=0.5)
plt.xlabel("Data", size=14)
plt.ylabel("Count", size=14)
plt.title("Drinking Game Averages Over {} Games".format(amount_of_games))
plt.legend(loc='upper right')
plt.show()
