import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
car_manager = CarManager()
score = Scoreboard()

screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    for tracks in car_manager.all_track:
        for cars in tracks:
            if player.distance(cars) < 25:
                score.game_over()
                game_is_on = False

    if player.ycor() > 280:
        player.reset_position()
        car_manager.increase_speed()
        car_manager.reset_car()
        score.update_score()

    time.sleep(0.1)
    car_manager.move_car()

    screen.update()

screen.exitonclick()
