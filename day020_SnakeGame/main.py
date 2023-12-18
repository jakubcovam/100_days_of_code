# ------------------------------------------------------
# The Snake Game
# ------------------------------------------------------
"""
- there is a snake made out of three segments
- the snake can go up, down, left and right (changed by the cursor keys)
- user have to feed the snake with the food which appear on the screen (blue circles)
- by eating the food, the snake becomes bigger
- computer calculates the score which is printed on the screen
- the game ends if there is a collision with the wall or tail
- the 'game over' sign is also printed on the screen at the end of the game
"""
# ------------------------------------------------------
# Import libraries
# ------------------------------------------------------
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
# ------------------------------------------------------

# ------------------------------------------------------
# Run the code
# ------------------------------------------------------
# Set the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Create new snake, food and score from classes
snake = Snake()
food = Food()
score = Scoreboard()

# Change the direction of the movement by user input
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Move the snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
# ------------------------------------------------------
