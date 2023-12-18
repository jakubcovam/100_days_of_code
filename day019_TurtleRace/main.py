# ------------------------------------------------------
# The Turtle Race
# ------------------------------------------------------
"""
- there are 6 colored turtles
- the starting line is on the left side of the screen, the finish is on the right side of the screen
- each turtle moves forward by random number of steps (from 0 to 10)
- before the race, user tries to bet the color of a turtle which will win the race
- after the race, computer print out the winner
"""
import turtle
# ------------------------------------------------------
# Import libraries
# ------------------------------------------------------
from turtle import Turtle, Screen
import random
# ------------------------------------------------------

# ------------------------------------------------------
# Run the code
# ------------------------------------------------------
is_race_on = False

# Set the screen
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color ('red', "
                                                          "'orange', 'yellow', 'green', 'blue', 'purple'): ").lower()
# print(user_bet)

# Set colors of the turtles
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Set the starting y-position
y_position = [-70, -40, -10, 20, 50, 80]

# Set the turtles
all_turtles = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

# Start the race
while is_race_on:
    for turtle in all_turtles:
        # check the finishing line
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle is the winner")
            else:
                print(f"You have lost! The {winning_color} turtle is the winner")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
# ------------------------------------------------------
