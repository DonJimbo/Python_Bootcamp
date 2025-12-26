#TODO 1 - Convert the guess to Title case - DONE
#TODO 2 - Check if the guess is among the 50 states -
#TODO 3 - Write correct guess onto the map
#TODO 4 - Use a loop to allow the user to keep guessing
#TODO 5 - Record the correct guesses in a list
#TODO 6 - Keep track of the course


import turtle
import pandas

'''Main answer'''

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame (missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
        #or t.write(state_data.state.item())

screen.exitonclick()

''' Alternative Answer'''
#    from turtle import Screen

#    turtle = Turtle()
#    screen = Screen()
#    screen.title("U.S. States Game")
#    image = "blank_states_img.gif"
#    screen.addshape(image)
#    turtle.shape(image)

#    data = pandas.read_csv("50_states.csv")
#    states = [data.state]
#    correct_guesses = []
#    correct_guesses_count = 0
#    game_on = True

#    while correct_guesses_count != 50:
#        game_on = True
#        answer_state = screen.textinput(title=f"Guess the state {correct_guesses_count}/50",prompt="What's another state's name?").title()
#
#        for state in states:
#            if answer_state != state:
#                pass
#            if answer_state == "Exit":
#                break
#            else:
#                state_name = data[data.state == f"{answer_state}"]
#                state_x = state_name.x
#                state_y = state_name.y
#                turtle.teleport(state_x.item(),state_y.item())
#                correct_guesses_count += 1
#                correct_guesses.append(state)
#    else:
#        game_on = False


