import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkeypress(fun = player.up, key = "w")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.level()

    if random.choice([1, 2, 3, 4, 5, 6]) == 6:
        print("Creating a car")
        car_manager.create_car()

    car_manager.movement()

    if player.ycor() > 280:
        scoreboard.update_score()
        player.start_over()
        car_manager.move_increase()

    for car in car_manager.cars:
        if player.distance(car) <= 20:
            restart = screen.textinput(title="Game Over", prompt="You hit a car! If you want to restart put 'yes'")
            if restart == "yes":
                player.start_over()
                scoreboard.score = 0
                car_manager.speed = 5
                for car in car_manager.cars:
                    car.hideturtle()
                car_manager.cars.clear()
                screen.listen()
                screen.onkeypress(fun=player.up, key="w")
            else:
                game_is_on = False
                screen.bye()

screen.exitonclick()

# Course answer code

"""
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update() 
    
    car_manager.create_car() 
    car_manager.move_cars()
    
    # Detect collision with the car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
    
    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
        
screen.exitonclick()

            

"""