from typing import final

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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# inputs with different inputs. 1 - off / 2 - coffee serving / 3 - report / 4 - coins
    # TODO (General) off -> machine (coffee serving) doesn't work
    # TODO (General) report -> show the current values of the "resources" library
    # TODO (Especifico) coffee serving ->
        # Check the current values of the "resources" library
            # if they aren't enough -> state f"Sorry there is not enough {resource}"
            # if they are enough -> continue
                # (Especifico) coins - >
                    # The user coins are processed, counting their value and adding to an account
                    # ¿Has the user inserted the correct coins amount to fulfil the coffee price?
                        # No -> "Sorry that's not enough money. Money refunded.”
                            # Refund of the money
                        # Yes ->
                            # Recognition of the price -> add money to the machine "wallet" (create a money variable)
                            # The user account is subtracted with the product price, return the use the "extra" amount.
        # The coffee is done, and exits a subtraction on the materials report.
    # TODO END -> Output a message f"Here is your {DRINK}. Enjoy!"


first_q = input ("What would you like? (espresso/latte/cappuccino):")
money = 0

def check():
    res_check_1 = MENU[f'{first_q}']['ingredients']['water'] <= resources['water']
    res_check_2 = MENU[f'{first_q}']['ingredients'].get('milk',0) <= resources['milk']
    res_check_3 = MENU[f'{first_q}']['ingredients']['coffee'] <= resources['coffee']
    resource_checks  = {
        'water':res_check_1,
        'milk':res_check_2,
        'coffee':res_check_3
        }

    missing_resources = [resource for resource, check in resource_checks.items() if not check]

    if first_q == "espresso":
        if res_check_1 and res_check_3:
            coins()
        else:
            print(f"Sorry there is not enough {', '.join(missing_resources)}")

    elif first_q in ["latte", "cappuccino"]:
        if res_check_1 and res_check_2 and res_check_3:
            coins()
        else:
            print(f"Sorry there is not enough {', '.join(missing_resources)}")

    else:
        print("No")

def coins():
    global first_q
    print("Please insert coins.")
    quarters = 0
    dimes = 0
    nickles = 0
    pennies = 0
    quarters = float(input("How many quarters?:")) * float(0.25)
    dimes = float(input("How many dimes?:")) * float(0.10)
    nickles = float(input("How many nickles?:")) * float(0.05)
    pennies = float(input("How many pennies?:")) * float(0.01)
    money_user = round(quarters + dimes + nickles + pennies,2)

    cost = MENU[f'{first_q}']['cost']
    refund = 0

    if money_user < cost:
        print("Sorry that's not enough money. Money refunded.")
        refund = money_user
        return print(f"The money refunded: ${refund}")
    elif money_user >= cost:
        refund = money_user - cost
        global money
        money += cost
        print(f"Here is ${refund} in change.")
        resource_subtraction()
        print(f"Here is your {first_q}. Enjoy!")
        continuation = input("What would you like? (espresso/latte/cappuccino):")
        first_q = continuation
        print(first_q)
        machine()

def resource_subtraction():
    if first_q == "espresso":
        resources['water'] -= MENU[f'{first_q}']['ingredients']['water']
        resources['milk'] -= MENU[f'{first_q}']['ingredients'].get('milk',0)
        resources['coffee'] -= MENU[f'{first_q}']['ingredients']['coffee']
    elif first_q in ["latte", "cappuccino"]:
        resources['water'] -= MENU[f'{first_q}']['ingredients']['water']
        resources['milk'] -= MENU[f'{first_q}']['ingredients']['milk']
        resources['coffee'] -= MENU[f'{first_q}']['ingredients']['coffee']
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")

def machine ():
    on = True
    global first_q

    if first_q == "off":
        return
    elif first_q == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
        continuation = input("What would you like? (espresso/latte/cappuccino):")
        first_q = continuation
        print(first_q)
        machine()
    elif first_q == "espresso" or first_q =="latte" or first_q =="cappuccino":
        check()
    else:
        print("Please select a correct mode")
        continuation = input("What would you like? (espresso/latte/cappuccino):")
        first_q = continuation
        print(first_q)
        machine()

machine()
