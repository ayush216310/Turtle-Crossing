from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager():

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle(shape="square")
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.goto(300, random.randint(-250, 250))
            new_car.left(180)
            self.all_cars.append(new_car)

    def move_car(self):
        for cars in self.all_cars:
            cars.forward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT