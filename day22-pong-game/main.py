#!/usr/bin/env python3

from court import Court
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

court = Court()
r_paddle = Paddle(court, "Up", "Down", 350, 0)
l_paddle = Paddle(court, "w", "s", -350, 0)
ball = Ball(court)
scoreboard = Scoreboard()

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    if ball.is_off_court_left():
        scoreboard.r_point()
        ball.reset_right()
    if ball.is_off_court_right():
        scoreboard.l_point()
        ball.reset_left()
    ball.bounce_left_if_hitting(r_paddle)
    ball.bounce_right_if_hitting(l_paddle)
    ball.move()
    court.update()

court.exit_on_click()
