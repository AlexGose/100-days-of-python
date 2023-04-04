#!/usr/bin/env python3

from court import Court
from paddle import Paddle

court = Court()
paddle = Paddle(court)

court.exit_on_click()
