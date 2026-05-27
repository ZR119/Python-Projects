#Ivan
#race between tortase and hare

import random

# Initial Conditions
finish_line = 50  #Finish Line
tortoise_pos = 0  #Starting Position
hare_pos = 0		 #Starting Position
hare_asleep = False #Hare starts Awake



# The Simulation Loop
while tortoise_pos < finish_line and hare_pos < finish_line:
# Tortoise always moves a short distance between 1 - 3 meters at random
    tortoise_pos = tortoise_pos + random.randint(1,3)
# Hare has a 30% chance of falling a sleep for a turn
    asleep_number = random.randint(1,100)
    if asleep_number <= 30:
        hare_asleep = True
# If Hare is awake, it will move 1 - 10 meters at random
    if hare_asleep == False:
        hare_pos = hare_pos + random.randint(1,10)
# Print the positions of the Hare and Tortoise after each round
    print("Tortoise", tortoise_pos, "l" , "Hare",  hare_pos)

# Determine the winner
    if tortoise_pos >= finish_line:
        print("🐢 The Tortoise wins!")
    if hare_pos >= finish_line:
        print("🐇 The Hare wins!")
