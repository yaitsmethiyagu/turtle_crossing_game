from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
TRACKS = 6


def add_car(direction):
    car = Turtle()
    car.shape("square")
    car.color(random.choice(COLORS))
    car.penup()
    car.shapesize(stretch_len=random.randint(1, 2), stretch_wid=1)
    car.setheading(direction)
    return car


def initiate_track():
    new_track = []
    heading = random.choice([0, 180])
    for i in range(random.randint(3, 7)):
        new_track.append(add_car(0))
    for cars in new_track:
        cars.setx(random.randrange(-290, 290))
        cars.setheading(heading)
    return new_track


def initiate_many_track(many):
    all_track = []

    for i in range(many):
        track_of_car = initiate_track()
        all_track.append(track_of_car)
    return all_track


class CarManager:

    def __init__(self):
        self.move_increment = MOVE_INCREMENT

        self.all_track = initiate_many_track(TRACKS)

        self.position_cars()

    def move_car(self):
        for tracks in self.all_track:
            for cars in tracks:

                if cars.xcor() > 340:
                    cars.setx(-340)
                elif cars.xcor() < -340:
                    cars.setx(340)
                cars.forward(self.move_increment)

    def position_cars(self):
        yposition = - 220
        increment = (280 * 2) / TRACKS

        for track in self.all_track:

            for cars in track:
                cars.sety(yposition)
            yposition += increment

    def increase_speed(self):
        self.move_increment += 5

    def reset_car(self):
        for tracks in self.all_track:
            for cars in tracks:
                cars.color(random.choice(COLORS))
                random_x = random.randrange(40, 150)
                cars.setx(cars.xcor() + random_x)
