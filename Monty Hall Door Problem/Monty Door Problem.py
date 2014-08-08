import random

random.seed()

#Change switch to whether or not you would like to switch 
#  after being shown the first door.
switch = True
wins = 0
losses = 0
iterations = 100000

#Change second parameter of range to change number range
for i in range (0,iterations):
    doors = ["car", "goat","goat"]
    indexes = [0,1,2]
    random.shuffle(doors)
    random.shuffle(indexes)
    door_number = indexes.pop()
    if doors[indexes[0]] == "goat" and switch:
        door_number = indexes[1]
    elif doors[indexes[1]] == "goat" and switch:
        door_number = indexes[0]
        
    if doors[door_number] == "car":
        wins = wins + 1
    else:
        losses = losses + 1

print ("Wins = %d, Losses = %d, ratio of wins to losses = %.4f" %(wins, losses ,float(wins)/iterations))
    
    
    

