# The football.csv file contains the results from the English Premier League.
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of
# goals scored for and against each team in that season (so Arsenal scored 79 goals
# against opponents, and had 36 goals scored against them). Write a program to read the file,
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.


# This is assuming by 'smallest difference' the meaning was the lowest absolute value.
# If it is the smallest numerical value, then the absolute (abs) function would not be used.

import pandas as pd

data = pd.read_csv('football.csv')
data['GD'] = data['Goals'] - data['Goals Allowed']
data.Team[abs(data.GD).idxmin()]
