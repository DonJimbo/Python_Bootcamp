import time
from player import Player
from turtle import Screen
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
score = Scoreboard()

screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("The Pong Game!")
screen.tracer(0)

player_1 = Player (-350,0)
player_2 = Player (350,0)
ball = Ball()

screen.listen()
screen.onkeypress(player_1.up1, "w")
screen.onkeypress(player_1.down1,"s")
screen.onkeypress(player_2.up1, "o")
screen.onkeypress(player_2.down1,"l")

game_on = True
while game_on:
    screen.update()
    ball.f_movement()
    time.sleep(ball.move_speed)

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.y_bounce()
        ball.speed_ball()

    elif ball.xcor() == player_1.xcor()+10 or ball.xcor() == player_2.xcor()-10:
        ball.speed_ball()
        if ball.distance(player_1) <= 10 or ball.distance(player_2) <= 10:
            ball.x_bounce()
        elif player_2.ycor() - 50 < ball.ycor() < player_2.ycor() + 50 or player_1.ycor() - 50 < ball.ycor() < player_1.ycor() + 50:
            ball.x_bounce()

    if ball.xcor() > 380:
        ball.reset_position()
        score.r_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score.l_point()

    for i in range (100):
        print(ball.xcor(),"||",ball.ycor()-40)
        print(ball.xcor(),"||",ball.ycor()+40)
        print(player_2.xcor()-10,"||",player_2.ycor())
        print(player_1.xcor()+10,"||",player_1.ycor())
        print("Dist p_1 ", ball.distance(player_1), "| Dist p_2:", ball.distance(player_2))
        print(ball.move_speed)

screen.exitonclick()



