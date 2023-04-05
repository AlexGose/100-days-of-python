from turtle import Turtle

WIDTH = 1  # stretch factor
LENGTH = 5  # stretch factor
SPEED = 20


class Paddle(Turtle):

    def __init__(self, court, up_key, down_key, x, y):
        super().__init__()
        self.court = court
        self.up_key = up_key
        self.down_key = down_key
        self.x = x
        self.y = y
        self.height = 20 * LENGTH
        self.width = 20 * WIDTH
        self.draw_paddle()
        self.add_key_movements()

    def move_up(self):
        if self.ycor() < self.court.height / 2 - self.height / 2:
            self.forward(SPEED)

    def move_down(self):
        if self.ycor() > - self.court.height / 2 + self.height / 2:
            self.back(SPEED)

    def add_key_movements(self):
        self.court.listen()
        self.court.on_key(self.move_up, self.up_key)
        self.court.on_key(self.move_down, self.down_key)

    def draw_paddle(self):
        self.speed("fastest")
        self.shape("square")
        self.shapesize(stretch_wid=WIDTH, stretch_len=LENGTH)
        self.color("white")
        self.penup()
        self.goto(self.x, self.y)
        self.setheading(90)
