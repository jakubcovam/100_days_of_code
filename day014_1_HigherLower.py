# ------------------------------------------------------
# Higher Lower Game
# ------------------------------------------------------
'''
- computer randomly choose two oponents from a dataset (day014_1_HigherLower_GameDat.py)
- user is trying to guess, which oponent has larger number of followers
- if the guess is correct, there is a new oponent to compare to
- the game ends when the user make a mistake

'''
# ------------------------------------------------------
# Import libraries
# ------------------------------------------------------
import random
import logos
from day014_1_HigherLower_GameData import data
# ------------------------------------------------------

# ------------------------------------------------------
# Define functions for running the game
# ------------------------------------------------------
def get_random():
    """Get random value from the range of the data."""
    random_choose = random.randint(0, len(data)-1)    
    return random_choose


def compare(item_A, item_B):
    """Compare user's guess and the correct number of followers."""
    if item_A >= item_B:
        return 'A'
    else:
        return 'B'


def higher_lower_game():
    """Run the game until there is a mistake. Count current score."""
    choose_A = get_random()
    current_score = 0
    
    is_correct = False
    while not is_correct:
        choose_B = get_random()
       
        print(logos.logo_higher_lower)
        print(f"Compare A: {data[choose_A]['name']}, {data[choose_A]['description']}, from {data[choose_A]['country']}.")
        print(logos.logo_vs)
        print(f"Against B: {data[choose_B]['name']}, {data[choose_B]['description']}, from {data[choose_B]['country']}.")
        
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        current_score += 1
        answer = compare(data[choose_A]['follower_count'], data[choose_B]['follower_count'])
    
        if guess == answer:
            print(f"You are right! Current score: {current_score}.")
            choose_A = choose_B
        else:
            print(f"Sorry, that is wrong. Final score: {current_score}.")
            is_correct = True
# ------------------------------------------------------

# ------------------------------------------------------
# Run the game
# ------------------------------------------------------
higher_lower_game()
# ------------------------------------------------------

