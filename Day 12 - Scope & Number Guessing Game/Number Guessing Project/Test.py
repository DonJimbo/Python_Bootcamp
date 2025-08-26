imfrom art import logo
import random

print(logo)

random_number = int(random.randint(1, 100))


print("I'm thinking a number between 1 and 100")


def play_game():
    global random_number
    num = random_number
    game_mode = input("Choose a difficulty. Type 'easy' or 'hard':\n")
    attempts = 0
    if game_mode.lower() == "hard":
        attempts = 5
    elif game_mode.lower() == "easy":
        attempts = 10

    print(game_mode)
    print(attempts)

    game = True
    while game is True:
        guess_number = int(input("Make a guess:"))
        print(f"--{num}--")
        print(guess_number)
        if guess_number > num:
            attempts -= 1
            print(f"{attempts}")
            print(f"--{num}--")
            print("Too High")
        elif guess_number < num:
            attempts -= 1
            print(f"{attempts}")
            print(f"--{num}--")
            print("Too Low")
        elif guess_number == num:
            print("You win! :)")
            game = False

        if attempts == 0:
            print("You lose :(")
            game = False
play_game()