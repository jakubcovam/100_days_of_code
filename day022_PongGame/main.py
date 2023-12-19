# ------------------------------------------------------
# The Pong Game
# ------------------------------------------------------
"""
- pong game for two players
- there are two paddles, one on the left and the other of the right side
- right paddle is controlled by 'up' and 'down' arrows, left paddle by 'w' and 's' keys
- there is a ball bouncing between the sides
- each player has to reflect the ball with his paddle
- if the ball hit the right or the left wall, another round starts and the scores are updated
- if the ball hit the bottom or the top wall, the ball is reflected and the game continues
- after reflecting of the ball with the paddle, the speed of the ball increased a little
"""
# ------------------------------------------------------
# Import libraries
# ------------------------------------------------------
from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

# ------------------------------------------------------

# ------------------------------------------------------
# Run the code
# ------------------------------------------------------
# Set the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# Create paddles, ball, scoreboard
r_paddle = Paddle("magenta", (350, 0))
l_paddle = Paddle("blue", (-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Move the paddle using 'up' and 'down' keys
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# Play the game
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when r_paddle missed the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect when l_paddle missed the ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
# ------------------------------------------------------
