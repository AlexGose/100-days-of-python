#!/usr/bin/env python3

from court import Court
from paddle import Paddle

court = Court()
paddle = Paddle(court)

game_is_on = True

while game_is_on:
    court.update()

court.exit_on_click()
