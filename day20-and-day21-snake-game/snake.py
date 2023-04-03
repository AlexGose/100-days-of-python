from turtle import Turtle
MOVE_DISTANCE = 20
UP_ANGLE = 90
DOWN_ANGLE = 270
LEFT_ANGLE = 180
RIGHT_ANGLE = 0


class Snake:
    def __init__(self):
        self.segments = []  # initialize with 3 white squares
        for turtle_index in range(3):
            self.add_segment(- 20 * turtle_index, 0)
        self.head = self.segments[0]

    def add_segment(self, x, y):
        next_turtle = Turtle(shape='square')
        next_turtle.color('white')
        next_turtle.penup()
        next_turtle.goto(x, y)
        self.segments.append(next_turtle)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN_ANGLE:
            self.head.setheading(UP_ANGLE)

    def down(self):
        if self.head.heading() != UP_ANGLE:
            self.head.setheading(DOWN_ANGLE)

    def left(self):
        if self.head.heading() != RIGHT_ANGLE:
            self.head.setheading(LEFT_ANGLE)

    def right(self):
        if self.head.heading() != LEFT_ANGLE:
            self.head.setheading(RIGHT_ANGLE)
