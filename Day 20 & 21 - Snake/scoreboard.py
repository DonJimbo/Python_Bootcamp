from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0

        self.color("white")
        self.hideturtle()
        self.penup()


    def update_scoreboard (self):
        self.clear()
        self.goto(0, 270)
        self.write(arg=f"Score = {self.score} High Score: {self.high_score}" , move=True, align="center", font=("Arial",14,"normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()


    #def game_over (self):
    #    self.goto(0, 0)
    #    self.#write("GAME OVER",align="center", font=("Arial",24,"normal"))








