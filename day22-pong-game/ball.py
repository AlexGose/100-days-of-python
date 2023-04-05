from turtle import Turtle

SPEED = 10


class Ball(Turtle):

    def __init__(self, court):
        super().__init__(shape='circle')
        self.court = court
        self.color("white")
        self.penup()
        self.dx = SPEED
        self.dy = SPEED

    def move(self):
        if self.is_hitting_wall():
            self.bounce_off_wall()

        self.goto(self.xcor() + self.dx, self.ycor() + self.dy)

    def is_hitting_wall(self):
        return self.ycor() >= self.court.height / 2 or self.ycor() <= -self.court.height / 2

    def bounce_off_wall(self):
        self.dy = - self.dy
