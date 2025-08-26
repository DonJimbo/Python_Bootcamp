import random
from colorsys import rgb_to_hls, rgb_to_hsv, rgb_to_yiq
from turtle import Turtle, Screen



#Challenge 1
'''
rgb_list = []
colors = colorgram.extract('image.jpg', 10000)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    colore = (r,g,b)
    rgb_list.append(colore)

print("-"*5)
print(rgb_list)
'''

#Challenge 2
color_list = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102), (66, 64, 60), (219, 178, 183), (178, 198, 202), (112, 139, 141), (254, 194, 0)]
tim = Turtle ()
tim.speed(9)
tim.penup()
tim.hideturtle()

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % rgb

def dot ():
    color = random.choice(color_list)
    hex_color = rgb_to_hex(color)
    tim.dot(20, hex_color)

a = -200
for y in range(10):
    tim.goto(-300, a)
    for x in range (10):
        tim.forward(50)
        dot()
    a += 50

Screen().exitonclick()


'''

from turtle import Turtle, Screen
timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")

# Challenge 1
for _ in range(4):
    timmy.forward(100)
    timmy.left(90)
'''

'''
def move_right ():
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)

move_right()
move_right()
move_right()
move_right()
'''