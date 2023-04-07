from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.show_score()

    def show_score(self):
        self.penup()
        self.hideturtle()
        self.goto(-200, 250)
        self.write(f"Score: {self.score}", font=FONT)

    def update(self):
        self.score += 1
        self.reset()
        self.show_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)
