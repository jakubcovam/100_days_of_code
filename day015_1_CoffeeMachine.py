# ------------------------------------------------------
# The Coffee Machine
# ------------------------------------------------------
'''
- computer asks about your choice (espresso, latte, cappuccino)
- user insert some coins
- computer checks if he has enough money and ingredients, then serves you the drink
- user can display a report of ingredients and machine profit, or turn the machine off
'''
# ------------------------------------------------------
# Import libraries
# ------------------------------------------------------
import logos
# ------------------------------------------------------

# ------------------------------------------------------
# Define needed functions
# ------------------------------------------------------
def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")
# ------------------------------------------------------

# ------------------------------------------------------
# Define variables
# ------------------------------------------------------
# coffee machine offer
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# profit of the coffee machine
profit = 0

# starting amounts of ingredients
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# ------------------------------------------------------

# ------------------------------------------------------
# Run the coffee machine
# ------------------------------------------------------
print(logos.logo_coffee)

is_on = True

while is_on:
    choice = input("​What would you like? ('espresso'/'latte'/'cappuccino' or 'report' or 'off'): ").lower()
    if choice == 'off':
        print("Goodbye!")
        is_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif choice == 'espresso' or choice == 'latte' or choice =='cappuccino':
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
    else:
        print("Sorry, this is not a valid choice. Please, choose again.")
# ------------------------------------------------------

