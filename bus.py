from turtle import Turtle

colour = ["red", "blue", "green", "yellow", "black", "orange"]
START_MOVING = 10
MOVE_INCREMENT=10
import random


class Bus(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.car = []
        self.bus_speed=START_MOVING

    def create_bus(self):
        random_chance = random.randint(1, 6)
        if random_chance == 6:
            new_bus = Turtle("square")

            new_bus.shapesize(stretch_wid=1, stretch_len=3)
            new_bus.penup()
            new_bus.color(random.choice(colour))
            random_y = random.randint(-250, 250)
            new_bus.goto(300, random_y)
            self.car.append(new_bus)

    def move_bus(self):
        for bus in self.car:
            bus.backward(self.bus_speed)

    def level_up(self):
        self.bus_speed+=MOVE_INCREMENT