from turtle import Turtle

WIDTH = 1
LENGTH = 5
SPEED = 20


class Paddle(Turtle):

    def __init__(self, court):
        super().__init__()
        self.court = court
        self.draw_paddle()
        self.add_key_movements()

    def move_up(self):
        if self.ycor() < self.court.height / 2 - 10 * LENGTH:
            self.forward(SPEED)

    def move_down(self):
        if self.ycor() > - self.court.height / 2 + 10 * LENGTH:
            self.back(SPEED)

    def add_key_movements(self):
        self.court.listen()
        self.court.on_key(self.move_up, "Up")
        self.court.on_key(self.move_down, "Down")

    def draw_paddle(self):
        self.hideturtle()
        self.speed("fastest")
        self.shape("square")
        self.shapesize(stretch_wid=WIDTH, stretch_len=LENGTH)
        self.color("white")
        self.penup()
        self.goto(350, 0)
        self.setheading(90)
        self.showturtle()
