def my_function():
  print("Hello")
  print("Bye")

my_function()

# Reeborg's World Code 
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def over_hill_loop():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# for loop for the jump
for step in range(6):
    over_hill_loop()

# while loop for the jump
number_of_hurdles = 6
while number_of_hurdles > 0:
    over_hill_loop()
    number_of_hurdles -= 1

#ways to write false in a while loop
while at_goal() == False:
    over_hill_loop()

while at_goal() != True:
    over_hill_loop()

while not at_goal():
    over_hill_loop()

#https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json