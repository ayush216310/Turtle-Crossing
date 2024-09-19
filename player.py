from turtle import Turtle
from scoreboard import Scoreboard
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
scoreboard = Scoreboard()
class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.goto(STARTING_POSITION)
        self.left(90)

    def move_foward(self):
        self.forward(MOVE_DISTANCE)

    def move_backward(self):
        if self.ycor() > -280:
            self.left(180)
            self.move_foward()
            self.left(180)

    def check_move(self):
        if self.ycor() == FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True
        else :
            return False
