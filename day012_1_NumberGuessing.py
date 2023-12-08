# ------------------------------------------------------
# Number guessing game
# ------------------------------------------------------

# ------------------------------------------------------
# Import libraries
# ------------------------------------------------------
import random
import logos
# ------------------------------------------------------

# ------------------------------------------------------
# Define a function for running the game
# ------------------------------------------------------
def guessing_game():
    """You guess a number and it gives you a feedback if it is correct."""
    print(logos.logo_guessing)
    print("Welcome to the Number Guessing Game!")
    print("I am thinking af a number between 1 and 100.")
    
    # Randomly select target number from 1 to 100
    target_number = random.randint(1, 100)
    
    # Deal with difficulty
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': " )
    if difficulty == 'easy':
        number_of_attempts = 10
    else:
        number_of_attempts = 5
    
    # Aks for guess until there is no more attempts, or until the user find the target number
    is_correct = False
    while number_of_attempts > 0 and is_correct == False:    
        print(f"You have {number_of_attempts} attemps remaining to gues the number.")
        
        guess = int(input("Make a guess: "))
    
        if guess == target_number:
            print("That is correct.")
            is_correct = True
        elif guess < target_number:
            print("Too low.")
        else:
            print("Too high.")
            
        number_of_attempts -=1
    
    if is_correct == True:
        print("Congratulation!")
    else:
        print("Sorry, you lose.")
# ------------------------------------------------------

# ------------------------------------------------------
# Run the game
# ------------------------------------------------------
# Run the game until the user wants to stop 
while input("Do you want to play a game? Type 'y' or 'n': ") == 'y':
    guessing_game()
# ------------------------------------------------------

