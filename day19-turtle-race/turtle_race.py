#!/usr/bin/env python3

from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtles = []
y = -100
for i in range(6):
    t = Turtle(shape='turtle')
    turtles.append(t)
    t.color(colors[i])
    t.penup()
    t.goto(x=-230, y=y)
    y += 40

if user_bet:
    is_race_on = True

winners = []
while is_race_on:
    for t in turtles:
        t.forward(random.randint(0, 10))
        if t.xcor() >= 230:
            winners.append(t)
    if winners:
        is_race_on = False
        user_won = False
        for winner in winners:
            winner_color = winner.pencolor()
            if winner_color == user_bet.lower():
                print(f"You won! The {winner_color} turtle is a winner!")
                user_won = True
            else:
                print(f"The {winner_color} turtle is a winner!")
        if not user_won:
            print(f"Sorry, you lose!")

screen.exitonclick()
