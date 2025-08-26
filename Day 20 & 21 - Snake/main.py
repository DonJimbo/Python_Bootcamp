import time
from snake import Snake
from turtle import Screen
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Second format

snake = Snake()
food = Food ()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun = snake.up,key = "w")
screen.onkey(fun = snake.down,key = "s")
screen.onkey(fun = snake.right,key = "d")
screen.onkey(fun = snake.left,key = "a")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    scoreboard.update_scoreboard()
    snake.movement()

    # Detect collision head with food
    if snake.head.distance(food) < 15:
        scoreboard.score += 1
        snake.extend()
        food.refresh()

    # Detect collision head with wall
    if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        scoreboard.reset()
        snake.reset()

    # Detect collision head with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 1:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()

# First format
'''
snake_length = 3
seg_list = []
x_list = []

for snake in range(snake_length):
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(-20 * snake, y= 0)
    seg_list.append(new_segment)
    print(seg_list)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    for seg in range (snake_length-1,0,-1):
        new_corx = seg_list[seg-1].xcor()
        print(new_corx)
        new_cory = seg_list[seg-1].ycor()
        print(new_cory)
        seg_list[seg].goto(new_corx,new_cory)
    seg_list[0].forward(20)
    seg_list[0].left(90)

'''

