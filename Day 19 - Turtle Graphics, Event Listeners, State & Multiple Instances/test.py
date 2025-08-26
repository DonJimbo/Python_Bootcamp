import turtle
from turtle import Turtle
from random import random,randrange

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

a = randrange (1, 10)
print(a)
