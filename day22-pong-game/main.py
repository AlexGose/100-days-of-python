#!/usr/bin/env python3

from court import Court
from paddle import Paddle
from ball import Ball
import time

court = Court()
r_paddle = Paddle(court, "Up", "Down", 350, 0)
l_paddle = Paddle(court, "w", "s", -350, 0)
ball = Ball(court)

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    ball.move()
    court.update()

court.exit_on_click()
