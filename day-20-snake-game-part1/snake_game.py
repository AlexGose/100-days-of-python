#!/usr/bin/env python3

from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

turtles = []  # initialize with 3 white squares
for turtle_index in range(3):
    next_turtle = Turtle(shape='square')
    next_turtle.color('white')
    next_turtle.setx(next_turtle.xcor() - 20 * turtle_index)
    turtles.append(next_turtle)

screen.exitonclick()
