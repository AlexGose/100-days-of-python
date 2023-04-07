from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__(shape='turtle')
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        self.sety(self.ycor() + MOVE_DISTANCE)

    def move_on_key_press(self, screen):
        screen.onkey(self.move_up, key="Up")
