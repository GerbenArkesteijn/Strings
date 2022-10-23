# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

player1 = "Ruud Gullit"
player2 = "Marco van Basten"
goal_0 = 32
goal_1 = 54

scorers = player1 + " " + str(goal_0) + ", " + player2 + " " + str(goal_1)
print(scorers)

report = f'{player1} scored in the {goal_0}nd minute\n{player2} scored in the {goal_1}th minute'
print(report)

player = "Hans van Breukelen"
first_name = player[:player.find(" ")]

last_name_temp = player[len(first_name):]
last_name = last_name_temp[1:]

print(first_name)
print(last_name)

last_name_len = len(last_name)
print(last_name_len)

name_short = player[0] + '. ' + player[len(first_name)+1:]
print(name_short)

shoutFirstName = first_name + '!' + " "
chant_temp = shoutFirstName * len(first_name)
chant = chant_temp[0:-1]
print(chant)

good_chant = chant[-1] != " "
print(good_chant)
