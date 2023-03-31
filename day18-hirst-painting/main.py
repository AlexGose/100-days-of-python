from turtle import Turtle, Screen
import turtle
import random

turtle.colormode(255)
tim = Turtle()
tim.hideturtle()
tim.penup()
tim.speed('fastest')

colors = [(243, 242, 239), (99, 6, 51), (172, 158, 33),
          (75, 94, 172), (232, 209, 73), (10, 35, 127)]


def draw_line_of_circles():
    for i in range(10):
        tim.dot(20, random.choice(colors))
        tim.forward(50)


def move_lower_left():
    tim.right(180)
    tim.forward(500)
    tim.left(90)
    tim.forward(500)
    tim.left(90)


def move_next_row():
    tim.left(180)
    tim.forward(500)
    tim.right(90)
    tim.forward(50)
    tim.right(90)


move_lower_left()
for _ in range(10):
    draw_line_of_circles()
    move_next_row()


screen = Screen()
screen.exitonclick()
