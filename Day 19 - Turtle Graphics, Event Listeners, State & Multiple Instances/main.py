import random
import turtle
from random import *
from turtle import Turtle, Screen

# Challenge 1
'''
tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def move_counterclockwise():
    tim.left(10)
    tim.forward(10)

def move_clockwise():
    tim.right(10)
    tim.forward(10)

def move_clear():
    tim.reset()

screen.listen()
screen.onkeypress(key = "W".lower(), fun = move_forward)
screen.onkeypress(key = "S".lower(), fun = move_backwards)
screen.onkeypress(key = "A".lower(), fun = move_counterclockwise)
screen.onkeypress(key = "D".lower(), fun = move_clockwise)
screen.onkey(key = "C".lower(), fun = move_clear)
screen.exitonclick()
'''

# Challenge 2
screen = Screen()
screen.setup(width=500,height=400)



tim = Turtle()
tim.shape("turtle")
tim.color("red")

one = Turtle()
one.shape("turtle")
one.color("blue")

dos = Turtle()
dos.shape("turtle")
dos.color("yellow")

tres = Turtle()
tres.shape("turtle")
tres.color("purple")

cuatro = Turtle()
cuatro.shape("turtle")
cuatro.color("pink")

turtles = (one,dos,tres,cuatro,tim)


def start ():
    for turtle in turtles:
        turtle.penup()
    tim.setposition(-230, 140)
    one.setposition(-230, 70)
    dos.setposition(-230, 0)
    tres.setposition(-230, -70)
    cuatro.setposition(-230, -140)
start()

bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race?")
print(f"Your:{bet}")

def main():
    for _ in range (250):
        for turtle in turtles:
            a = randrange(1, 10)
            turtle.forward(a)
            if turtle.xcor() > screen.window_height():
                turtle.forward(0)
                if turtle.color()[1] == bet:
                    screen.bye()
                    print(f"You won! The {turtle.color()[1]} turtle was first place.")
                else:
                    print(f"You lose! The {turtle.color()[1]} turtle won.")
                exit()

main()
screen.exitonclick()