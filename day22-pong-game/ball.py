from turtle import Turtle

SPEED = 10


class Ball(Turtle):

    def __init__(self, court):
        super().__init__(shape='circle')
        self.radius = 20
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
        self.dy *= -1

    def bounce_off_paddle(self):
        self.dx *= -1

    def is_hitting(self, paddle):
        return - self.radius / 2 - paddle.width / 2 <= self.xcor() - paddle.xcor() \
                <= paddle.width / 2 + self.radius / 2 and \
                - self.radius / 2 - paddle.height / 2 <= self.ycor() - paddle.ycor() \
                <= paddle.height / 2 + self.radius / 2

    def is_moving_right(self):
        return self.dx > 0

    def is_moving_left(self):
        return self.dx < 0

    def bounce_left_if_hitting(self, paddle):
        if self.is_hitting(paddle) and self.is_moving_right():
            self.bounce_off_paddle()

    def bounce_right_if_hitting(self, paddle):
        if self.is_hitting(paddle) and self.is_moving_left():
            self.bounce_off_paddle()
