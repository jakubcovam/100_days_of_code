# ------------------------------------------------------
# Turtle Crossing the Street
# ------------------------------------------------------
"""
- game for one player
- the goal is to cross a street without any collision with a car
- the turtle is controlled by the 'up' arrow
- if there is a collision with a car, the game ends
- if the player successfully cross the street, next level starts
- with increasing level, the car speed also increases
"""
# ------------------------------------------------------
# Import libraries
# ------------------------------------------------------
from turtle import Turtle, Screen
import random
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
# ------------------------------------------------------

# ------------------------------------------------------
# Run the code
# ------------------------------------------------------
# Set the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Street")
screen.tracer(0)

# Create a player, cars, scoreboard
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Move the player
screen.listen()
screen.onkey(player.go_up, "Up")

# Run the game
is_game_on = True
while is_game_on:
    time.sleep(0.1)
    screen.update()

    # Create and move cars
    car_manager.create_cars()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            is_game_on = False
            scoreboard.game_over()

    # Detect successful crossing and increase the speed
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()
# ------------------------------------------------------
