import turtle
turtle.setup(1200, 600)

gang = []
for x in range(100):
    gang.append(turtle.Turtle())
    gang[x].shape("turtle")

# change all the turtles' color
for brendan in gang:
    brendan.color("cyan")

# move all the turtles to a random spot
for marisa in gang:
    marisa.goto(50, 50)   # REMEMBER HOW TO MAKE RANDOM!?!? LOOK IT UP

# EXTRA: make all of the turtles with an even index write a message


input("Press enter to quit")
