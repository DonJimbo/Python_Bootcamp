"""
game_over = False
def coffee_start ():
    while game_over is not True:
        input(f"What kind of coffee do you want? (espresso/latte/cappuccino)")

        if input == "espresso":
            print("")
        elif input == "latte":
            print("")
        elif input == "cappuccino":
            print("")

coffee_start()

def coins():
    print("Please insert coins.")
    quarters = 0
    dimes = 0
    nickles = 0
    pennies = 0
    quarters = float(input("How many quarters?:")) * float(0.25)
    dimes = float(input("How many dimes?:")) * float(0.10)
    nickles = float(input("How many nickles?:")) * float(0.05)
    pennies = float(input("How many pennies?:")) * float(0.01)
    money = f"${round(quarters + dimes + nickles + pennies,2)}"
    # Add the substraction of the product price to the money provided by the customer.
    print (f"Here is {money} in change.")
coins()


def coffee():
"""
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

resources = {
    "water": 30,
    "milk": 20,
    "coffee": 10,
}

# ¿Has the user inserted the correct coins amount to fulfil the coffee price?
    # No -> "Sorry that's not enough money. Money refunded.”
        # Refund of the money
    # Yes ->
        # Recognition of the price -> add money to the machine "wallet" (create a money variable)
        # The user account is subtracted with the product price, return the use the "extra" amount.
            # The coffee is done, and exits a subtraction on the materials report.

def coins():
    money = 0
    print("Please insert coins.")
    quarters = 0
    dimes = 0
    nickles = 0
    pennies = 0
    quarters = float(input("How many quarters?:")) * float(0.25)
    dimes = float(input("How many dimes?:")) * float(0.10)
    nickles = float(input("How many nickles?:")) * float(0.05)
    pennies = float(input("How many pennies?:")) * float(0.01)
    money_user = f"${round(quarters + dimes + nickles + pennies,2)}"
    cost = MENU []


    # Add the substraction of the product price to the money provided by the customer.
    print (f"Here is {money} in change.")
