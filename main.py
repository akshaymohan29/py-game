from turtle import Turtle, Screen
from player import Player
from bus import Bus
from score import Score
import time

screen = Screen()

screen.bgcolor("coral")
screen.setup(width=600, height=600)
screen.title("turtle crossing")
screen.tracer(0)
player1 = Player()
bus1 = Bus()
score = Score()
screen.listen()
screen.onkey(player1.move, "Up")
is_game_on = True

while is_game_on:
    time.sleep(0.1)
    screen.update()
    bus1.create_bus()
    bus1.move_bus()
    for bus in bus1.car:
        if bus.distance(player1) < 20:
            is_game_on = False
            score.game_over()
    if player1.end():
        player1.go_to_start()
        bus1.level_up()
        score.increase_scor()

screen.exitonclick()
