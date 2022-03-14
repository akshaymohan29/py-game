from turtle import Turtle
STARTING_POSITION=(0,-280)
MOVE_DISTANCE=10
FINISHING_LINE=280

class Player(Turtle):
   def __init__(self):
       super().__init__()
       self.shape("turtle")
       self.color("red")
       self.penup()
       self.goto(STARTING_POSITION)
       self.left(90)

   def move(self):
       self.forward(MOVE_DISTANCE)

   def go_to_start(self):

       self.goto(0,-280)
   def end(self):
       if self.ycor()>FINISHING_LINE:
           return True
       else:
           return False


