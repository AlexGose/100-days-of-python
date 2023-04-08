from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = Scoreboard.read_high_score()
        self.pencolor("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.pendown()
        self.show_score()

    @staticmethod
    def read_high_score():
        with open('data.txt') as file:
            high_score = int(file.read())
        return high_score

    @staticmethod
    def write_high_score(high_score):
        with open('data.txt', 'w') as file:
            file.write(str(high_score))

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            Scoreboard.write_high_score(self.high_score)
        self.score = 0
        self.show_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.show_score()
