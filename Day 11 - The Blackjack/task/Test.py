import random
from art import logo
print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

entrance_question =input("You want to play? Say y or n:\n")
game_start = True

def game(game_start):

    c_player = []
    c_player_count = 0
    c_computer = []
    c_computer_count = 0

    if game_start:

        c_player += random.sample(cards, 2)
        c_player_count = sum(c_player)
        print(f"Your cards: {c_player}, current score {c_player_count}")

        c_computer += random.sample(cards, 1)
        c_computer_count = sum(c_computer)
        print(f"Computer's first card: {c_computer}, current score {c_computer_count}\n")


    while True:

        if c_player_count == 21:
            print("You win :D, you have Blackjack!")
            return False

        add = input("You want to continue? Say y or n:\n")
        if add.lower() == "y":
            c_player += random.sample(cards, 1)
            c_player_count = sum(c_player)
            print(f"Your cards: {c_player}, current score {c_player_count}")

            while c_player_count > 21 and 11 in c_player:
                c_player[c_player.index(11)] = 1
                c_player_count = sum(c_player)
                print(f"Your cards: {c_player}, current score {c_player_count}")

            if c_player_count > 21:
                print("You lose :(")
                return False

        elif add.lower() == "n":
            while c_computer_count < 17:
                c_computer += random.sample(cards, 1)
                c_computer_count = sum(c_computer)

            print(f"Your cards: {c_player}, current score {c_player_count}")
            print(f"Computer's first card: {c_computer}, current score {c_computer_count}\n")

            if c_computer_count == 21:
                print("You Lose :D, your opponent has Blackjack!")
            elif c_computer_count > 21:
                print("You Win :D")

            elif c_player_count == c_computer_count:
                print("Draw!")
            elif c_player_count > c_computer_count:
                print("You Win :D")
            elif c_player_count < c_computer_count:
                print("You Lose :D")

            print("End")
            return False

if entrance_question.lower() == "n":
    game_start = False
    print("End")

elif entrance_question.lower() == "y":
    while game_start:
        game_start = game (game_start)
