from turtle import Turtle


class Snake:
    def __init__(self):
        self.segments = []  # initialize with 3 white squares
        for turtle_index in range(3):
            next_turtle = Turtle(shape='square')
            next_turtle.color('white')
            next_turtle.penup()
            next_turtle.setx(next_turtle.xcor() - 20 * turtle_index)
            self.segments.append(next_turtle)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].left(90)
        self.segments[0].forward(20)
