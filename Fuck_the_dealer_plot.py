import matplotlib.pyplot as plt

file1 = '/Users/sebastiandhoore/Documents/PycharmProjects/personal_project/Drinking_Games/FTD_data/FTD_turns.txt'
file2 = '/Users/sebastiandhoore/Documents/PycharmProjects/personal_project/Drinking_Games/FTD_data/FTD_shots.txt'
file3 = '/Users/sebastiandhoore/Documents/PycharmProjects/personal_project/Drinking_Games/FTD_data' \
        '/FTD_shots_per_player_4.txt'
turns_file = open(file1, 'r')
shots_file = open(file2, 'r')
shots_pp4_file = open(file3, 'r')
turns = turns_file.read()
shots = shots_file.read()
shots_pp4 = shots_pp4_file.read()
turns_list = turns.split(", ")
shots_list = shots.split(", ")
shots_pp4_list = shots_pp4.split(", ")
turns_list = [int(x) for x in turns_list]
amount_of_games = len(turns_list)
shots_list = [int(x) for x in shots_list]
shots_pp4_list = [int(x) for x in shots_pp4_list]
player1_list = shots_pp4_list[0::4]
player2_list = shots_pp4_list[1::4]
player3_list = shots_pp4_list[2::4]
player4_list = shots_pp4_list[3::4]
plt.hist(turns_list, bins=30, label='Turns', alpha=0.5)
plt.hist(shots_list, bins=30, label='Shots', alpha=0.5)
plt.xlabel("Data", size=14)
plt.ylabel("Count", size=14)
plt.title("Fuck The Dealer Averages Over {} Games".format(amount_of_games))
plt.legend(loc='upper right')
plt.show()
plt.hist(player1_list, bins=30, label='Player 1', alpha=0.5)
plt.hist(player2_list, bins=30, label='Player 2', alpha=0.5)
plt.hist(player3_list, bins=30, label='Player 3', alpha=0.5)
plt.hist(player4_list, bins=30, label='Player 4', alpha=0.5)
plt.xlabel("Data", size=14)
plt.ylabel("Count", size=14)
plt.title("Fuck The Dealer Averages Per Player Over {} Games".format(amount_of_games))
plt.legend(loc='upper right')
plt.show()
