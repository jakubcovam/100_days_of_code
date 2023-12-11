# ------------------------------------------------------
# The BlackJack game
# ------------------------------------------------------
'''
- user and computer get randomly two cards, user can deal more cards as he wished and the scores are compared
- the aim is to have a score of 21
- cards are selected from a list with repetition, without given any specific probabilities to each card
'''
# ------------------------------------------------------
# Import libraries
# ------------------------------------------------------
import random
import logos
# ------------------------------------------------------

# ------------------------------------------------------
# Define needed functions
# ------------------------------------------------------
def deal_card():
    """Returns  a random card from the list."""
    all_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(all_cards)

def calculate_score(cards):
    """Returns a sum of all cards from the list."""
    if 11 in cards and sum(cards) > 21:  # Ace could be equal to 1 or 11
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def print_final(cards_your, score_your, cards_computer, score_computer):
    """Print final messages of your and computer's cards and scores.""" 
    print(f"  Your final hand: {cards_your}, final score: {score_your}")
    print(f"  Computer's final hand: {cards_computer}, final score: {score_computer}")
# ------------------------------------------------------

# ------------------------------------------------------
# Run the code
# ------------------------------------------------------
reset_game = True
while reset_game:
    print(logos.logo_blackjack)

    cards_your = []
    cards_computer = []

    for deal in range(2):
        cards_your.append(deal_card())
        cards_computer.append(deal_card())

    score_your = calculate_score(cards_your)
    score_computer = calculate_score(cards_computer)

    print(f"  Your cards: {cards_your}, current score: {score_your}")
    print(f"  Computer's first card: {cards_computer[0]}")
    
    want_next_card = True
    while want_next_card:
        if input("Type 'y' to get another card, type 'n' to pass: ") == 'y':
            cards_your.append(deal_card())
            score_your = calculate_score(cards_your)
            print(f"  Your cards: {cards_your}, current score: {score_your}")
            print(f"  Computer's first card: {cards_computer[0]}")
            
            if score_your > 21:        
                print_final(cards_your, score_your, cards_computer, score_computer)
                print("You went over. You lose.")
                want_next_card = False
            elif score_your == 21:
                print_final(cards_your, score_your, cards_computer, score_computer)
                print("You win.")  
                want_next_card = False    
        else:
            while score_computer < 17:
                cards_computer.append(deal_card())
                score_computer = calculate_score(cards_computer)
            
            print_final(cards_your, score_your, cards_computer, score_computer)
       
            if score_your == score_computer:
                print("It is a draw.")  
            elif score_your > score_computer or score_computer > 21:
                print("You win.")
            else:
                print("You are too low. You lose.")         
            want_next_card = False

    if input("Type 'y' to reset the game, type 'e' to exit the game: ") != 'y':
        reset_game = False
        
# ------------------------------------------------------

