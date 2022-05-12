# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

from re import sub


goalscorer_1 = 'Gullit'
goalscorer_2 = 'van Basten'

time_goal_1 = str(32)
time_goal_2 = str(54)

scorers = goalscorer_1 + time_goal_1, goalscorer_2 + time_goal_2

report = goalscorer_1 + ' scored in the ' + time_goal_1 + 'nd minute of the game, while '+ goalscorer_2 +' scored the second goal in the ' + time_goal_2 + 'th minute' 
print (report)
player = 'Frank Rijkaard'

first_name = player [0:5]

last_name_len = player [6:] 

name_short = player [0] + '. ' + player [6:14]

chant = (first_name + '!') * 5

print(chant)



