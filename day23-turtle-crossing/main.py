import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
car_manager = CarManager()

num_time_steps = 0
game_is_on = True
while game_is_on:
    num_time_steps += 1
    time.sleep(0.1)
    if num_time_steps % 6 == 0:
        car_manager.add_car()
    car_manager.move_cars(0)
    if car_manager.car_hitting(player):
        game_is_on = False
    player.move_on_key_press(screen)
    if player.finished_crossing():
        player.reset()
    screen.update()

screen.exitonclick()
