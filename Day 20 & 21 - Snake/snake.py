# Her format
from turtle import Turtle


STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVEMENT_STEPS = 20

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.degrees_up = 90
        self.degrees_down = 270
        self.degrees_right = 0
        self.degrees_left = 180
        self.head = self.segments[0]


    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment (self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset (self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend (self):
        self.add_segment(self.segments[-1].position())

    def movement(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_corx = self.segments[seg - 1].xcor()
            new_cory = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_corx, new_cory)
        self.head.forward(MOVEMENT_STEPS)

    def up (self):
        if self.head.heading() != self.degrees_down:
            self.head.setheading(self.degrees_up)
    def down (self):
        if self.head.heading() != self.degrees_up:
            self.head.setheading(self.degrees_down)
    def right (self):
        if self.head.heading() != self.degrees_left:
            self.head.setheading(self.degrees_right)
    def left (self):
        if self.head.heading() != self.degrees_right:
            self.head.setheading(self.degrees_left)

# My format
'''
from turtle import Turtle
class Snake:
    def __init__(self):
        self.shape = "square"
        self.color = "white"
        self.initial_position = [(0, 0), (-20, 0), (-40, 0)]
        self.seg_list = []
        self.create_snake()

    def create_snake(self):
        for position in self.initial_position:
            self.add_segment(position)

    def add_segment(self, initial_position):
        new_segment = Turtle(self.shape)
        new_segment.color(self.color)
        new_segment.penup()
        new_segment.goto(initial_position)
        self.seg_list.append(new_segment)

    def movement(self):
        for seg in range(len(self.seg_list) - 1, 0, -1):
            new_corx = self.seg_list[seg - 1].xcor()
            new_cory = self.seg_list[seg - 1].ycor()
            self.seg_list[seg].goto(new_corx, new_cory)
        self.seg_list[0].forward(20)
        self.seg_list[0].left(90)
'''


