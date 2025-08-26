import random
from art import logo


def cards_def ():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def card_swap (cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def constrains (c_player, c_computer):
    if c_player ==  c_computer:
        return "Draw"
    elif c_player == 0:
        return "You have Blackjack"
    elif c_computer == 0:
        return "They have Blackjack"
    elif c_player > 21:
        return "They pass yourself. You lose!"
    elif c_computer > 21:
        return "You pass yourself. You win!"
    elif c_player > c_computer:
        return "You win!"
    elif c_player < c_computer:
        return "You lose!"



def game_start ():
    print(logo)
    c_player = []
    sc_player = 0
    c_computer = []
    sc_computer = 0
    game_over = False

    for _ in range (2):
        c_player.append(cards_def())
        c_computer.append(cards_def())

    while not game_over:
        sc_player = card_swap(c_player)
        sc_computer = card_swap(c_computer)
        print(f"Your cards are {c_player}, and your score {sc_player}")
        print(f"Computer cards are {c_computer[0]}")

        if sc_player == 0 or sc_computer == 0 or sc_player > 21:
            game_over = True

        else:
            s_question = input("Type 'y' to get another card, type 'n' to pass: ")
            if s_question == "y":
                c_player.append(cards_def())
            else:
                game_over = True

    while sc_computer < 17 and sc_computer != 0:
        c_computer.append(cards_def())
        sc_computer = card_swap(c_computer)

    print(f"Your final hand: {c_player}, final score: {sc_player}")
    print(f"Computer's final hand: {c_computer}, final score: {sc_computer}")
    print(constrains(sc_player, sc_computer))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    game_start()










