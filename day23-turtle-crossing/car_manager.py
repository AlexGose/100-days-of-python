from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car(Turtle):

    def __init__(self):
        super().__init__(shape='square')
        self.penup()
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(180)
        self.goto(300, - 295 + 590 * random.random())

    def move(self, num_levels):
        self.forward(STARTING_MOVE_DISTANCE + num_levels * MOVE_INCREMENT)

    def car_drove_off_screen(self):
        return self.xcor() < - 320


class CarManager:

    def __init__(self):
        self.cars = []

    def add_car(self):
        self.cars.append(Car())

    def move_cars(self, num_levels):
        for car in self.cars:
            car.move(num_levels)
            if car.car_drove_off_screen():
                self.cars.remove(car)
