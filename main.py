# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

from re import sub

# Part 1

goalscorer_0 = 'Ruud Gullit'
goalscorer_1 = 'Marco van Basten'

goal_0 = 32
goal_1 = 54

scorers = goalscorer_0 + ' ' + str(goal_0) + ', ' + goalscorer_1 + ' ' + str(goal_1)

report = f'{goalscorer_0} scored in the {goal_0}nd minute\n{goalscorer_1} scored in the {goal_1}th minute' 

# Part 2

player = 'Frank Rijkaard'

first_name = player[:player.find(' ')]

last_name = player[player.find(' ')+1:] 

last_name_len = len(last_name)

first_name_short = player[0] 
name_short = first_name_short + '. ' + last_name

message = (first_name + '! ') * 5 
chant = message[0:len(message)-1]

good_chant = chant[len(chant)-1] != " "
