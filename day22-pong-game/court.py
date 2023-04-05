from turtle import Screen, Turtle

WIDTH = 800
HEIGHT = 600
DASH_LENGTH = 20
DASH_WIDTH = 5


class Court:
    def __init__(self):
        self.screen = Screen()
        self.width = WIDTH
        self.height = HEIGHT
        self.draw_screen()
        self.turtle = Turtle()
        self.draw_dashed_line()

    def draw_screen(self):
        self.screen.title("Pong")
        self.screen.bgcolor("black")
        self.screen.setup(width=WIDTH, height=HEIGHT)
        self.screen.tracer(0)

    def exit_on_click(self):
        self.screen.exitonclick()

    def listen(self):
        self.screen.listen()

    def on_key(self, fun, key):
        self.screen.onkey(fun, key)

    def update(self):
        self.screen.update()

    def draw_dashed_line(self):
        self.turtle.pensize(DASH_WIDTH)
        self.turtle.speed("fastest")
        self.turtle.penup()
        self.turtle.color("white")
        self.turtle.goto(0, - HEIGHT // 2)
        self.turtle.setheading(90)
        for _ in range(HEIGHT // (2 * DASH_LENGTH)):
            self.turtle.pendown()
            self.turtle.forward(DASH_LENGTH)
            self.turtle.penup()
            self.turtle.forward(DASH_LENGTH)
        self.turtle.hideturtle()
