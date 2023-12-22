## 💯 Days of Code 💪

My scripts from the **100 Days of Code: The Complete Python Pro Bootcamp for 2023** created by Dr. Angela Yu on udemy.com. The codes are sometimes different than the ones given by Angela, but everything seems to work as I planned. 


### ℹ️ logos.py
- ascii art with logos
- from https://ascii.co.uk/art or https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20

### ℹ️ day011_1_Blackjack.py
- BlackJack game
- user and computer get randomly two cards, user can deal more cards as he wished and the scores are compared
- the aim is to have a score of 21
- cards are selected from a list with repetition, without given any specific probabilities to each card

### ℹ️ day012_1_NumberGuessing.py
- Number Guessing Game
- computer choose a random number from 1 to 100 and the user has to guess the correct answer
- user choose from two difficulities: easy (10 attempts to guess the number) and hard (5 attempts)

### ℹ️ day014_1_HigherLower.py
- Higher/Lower game
- computer randomly choose two oponents from a dataset (day014_1_HigherLower_GameDat.py)
- user is trying to guess, which oponent has larger number of followers
- if the guess is correct, there is a new oponent to compare to
- the game ends when the user make a mistake

### ℹ️ day015_1_CoffeeMachine.py
- Coffee Machine software
- computer asks about your choice (espresso, latte, cappuccino)
- user insert some coins
- computer checks if he has enough money and ingredients, then serves you the drink
- user can display a report of ingredients and machine profit, or turn the machine off

### ℹ️ day017_QuizGame
- this game teaches you to use classes and modules in Python
- computer gives to the user a certain amount of questions
- user have to guess the answer (true/false)
- computer gives a feedback about the answer and calculates the score
- at the end, the final score of the quiz is printed
- trivia questions can be created via https://opentdb.com/api_config.php

### ℹ️ day019_TurtleRace
- this game teaches you basics from the 'turtle' class (https://docs.python.org/3/library/turtle.html)
- there are 6 colored turtles
- the starting line is on the left side of the screen, the finish is on the right side of the screen
- each turtle moves forward by random number of steps (from 0 to 10)
- before the race, user tries to bet the color of a turtle which will win the race
- after the race, computer print out the winner

### ℹ️ day020_SnakeGame
- there is a snake made out of three segments
- the snake can go up, down, left and right (changed by the cursor keys)
- user have to feed the snake with the food which appear on the screen (blue circles)
- by eating the food, the snake becomes bigger
- computer calculates the score which is printed on the screen
- the game ends if there is a collision with the wall or tail
- the 'game over' sign is also printed on the screen at the end of the game

### ℹ️ day022_PongGame
- pong game for two players
- there are two paddles, one on the left and the other of the right side
- right paddle is controlled by 'up' and 'down' arrows, left paddle by 'w' and 's' keys
- there is a ball bouncing between the sides
- each player has to reflect the ball with his paddle
- if the ball hit the right or the left wall, another round starts and the scores are updated
- if the ball hit the bottom or the top wall, the ball is reflected and the game continues
- after reflecting of the ball with the paddle, the speed of the ball increased a little

### ℹ️ day023_CrossingStreet
- game for one player
- the goal is to cross a street without any collision with a car
- the turtle is controlled by the 'up' arrow
- if there is a collision with a car, the game ends
- if the player successfully cross the street, next level starts
- with increasing level, the car speed also increases

### ℹ️ day028_Pomodoro
- an application, which help you manage your time
- 'work' for 25 minutes
- after each working session, there is 5 minutes for 'short break'
- after 4 working sessions, there is 20 minutes for 'long break'
- current time and activity is displayed
- user can start or reset the timer

### ℹ️ day029_GeneratePassword
- for creating passwords and saving them into a file
- user has to fill in the website name, email or username and password
- the password can be generated randomly from letters, numbers and symbols
- all inputs are saved as a new line in a file
