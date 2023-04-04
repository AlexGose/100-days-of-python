#!/usr/bin/env python3

from court import Court
from paddle import Paddle

court = Court()
r_paddle = Paddle(court, "Up", "Down", 350, 0)
l_paddle = Paddle(court, "w", "s", -350, 0)

game_is_on = True

while game_is_on:
    court.update()

court.exit_on_click()
