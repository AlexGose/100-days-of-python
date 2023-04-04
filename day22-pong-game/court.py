from turtle import Screen

WIDTH = 800
HEIGHT = 600


class Court:
    def __init__(self):
        self.screen = Screen()
        self.width = WIDTH
        self.height = HEIGHT
        self.draw_screen()

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
