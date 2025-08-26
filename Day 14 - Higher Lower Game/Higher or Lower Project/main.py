import random
from art import logo, vs
from game_data import data

# select 2 libraries

def famous():
    choice_1 = random.choice(data)
    choice_2 = random.choice(data)

    print(logo)
    print(f"Compare A: {choice_1['name']}, a {choice_1['description']}, from {choice_1['country']}.")
    print(choice_1['name'])
    print(choice_1['follower_count'])
    print(choice_1['description'])
    print(choice_1['country'])

    print(vs)
    print(f"Against B: {choice_2['name']}, a {choice_2['description']}, from {choice_2['country']}.")
    print(choice_2['name'])
    print(choice_2['follower_count'])
    print(choice_2['description'])
    print(choice_2['country'])

    return choice_1['follower_count'], choice_2['follower_count']


def constrains (a, b):
    if int(a) > int(b):
        print("a Higher than b")
    elif int(a) < int(b):
        print("Lower")
    elif int(a) == int(b):
        print("Correct")


#gmae
def game_start():
    game = True
    score = 0

    #a = choice_1['follower_count']
    # b = choice_2['follower_count']

    while game is True:
        print("="*20)
        a, b = famous()

        answer = input("Who has more followers? Type 'A' or 'B': ")
        if answer.lower() == "a":
            if int(a) > int(b):
                score += 1
                print(f"****You are right! Your scores is: {score}")
            elif int(a) < int(b):
                print(f"***Sorry, that's wrong! Your Final score was: {score}")
                game = False
        elif answer.lower() == "b":
            if int(a) < int(b):
                score += 1
                print(f"You are right! Your scores is: {score}")
            elif int(a) > int(b):
                print(f"Sorry, that's wrong! Your Final score was: {score}")
                game = False
game_start()



