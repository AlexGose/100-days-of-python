from turtle import Screen, Turtle

WIDTH = 800
HEIGHT = 600


class Court:
    def __init__(self):
        self.screen = Screen()
        self.draw_screen()

    def draw_screen(self):
        self.screen.title("Pong")
        self.screen.bgcolor("black")
        self.screen.setup(width=WIDTH, height=HEIGHT)

    def exit_on_click(self):
        self.screen.exitonclick()
