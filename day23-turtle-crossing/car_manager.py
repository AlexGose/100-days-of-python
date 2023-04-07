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
        self.goto(300, - 250 + 500 * random.random())

    def move(self, num_levels):
        self.forward(STARTING_MOVE_DISTANCE + num_levels * MOVE_INCREMENT)

    def drove_off_screen(self):
        return self.xcor() < - 320

    def is_hitting(self, player):
        abs_diff_y = abs(self.ycor() - player.ycor())
        abs_diff_x = abs(self.xcor() - player.xcor())
        return abs_diff_y < 20 and abs_diff_x < 30


class CarManager:

    def __init__(self):
        self.cars = []

    def add_car(self):
        self.cars.append(Car())

    def move_cars(self, num_levels):
        for car in self.cars:
            car.move(num_levels)
            if car.drove_off_screen():
                self.cars.remove(car)

    def car_hitting(self, player):
        for car in self.cars:
            if car.is_hitting(player):
                return True
        return False
