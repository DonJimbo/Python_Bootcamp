from turtle import Turtle

class Player(Turtle):
    def __init__(self, x_init, y_init):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(5,1)
        self.penup()
        self.goto(x_init,y_init)

    def up1 (self):
        self.goto(self.xcor(),self.ycor() + 20)

    def down1 (self):
        self.goto(self.xcor(),self.ycor() - 20)










