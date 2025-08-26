import random
from art import logo

easy = 5
hard = 10

def constrains (actual_answer, guess_answer, turns):
    if actual_answer > guess_answer:
        print("Too Low")
        turns -=1
    elif actual_answer < guess_answer:
        print("Too High")
        turns -=1
    else:
        print(f"You are right, the answer is: {actual_answer}")


def type_game(question):
    if question is "easy":
        return easy
    else:
        return hard

def game ():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number = random.randint(1,100)
    print(f"---{number}---")

    question = input("Please choose an 'easy' or 'hard' game:")
    turns = type_game(question)

    guess = 0
    while guess != number:
        guess = input("Please write your guess:")
        turns = constrains (number, guess, turns)
        if turns == 0:
            print("You don't have more attempts")
        elif guess == number:
            print(f"You are right, the answer is: {number}")

game()
