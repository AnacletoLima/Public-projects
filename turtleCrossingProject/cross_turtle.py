#100DaysOfCode
#TheAppBrewery

from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 300


class CrossTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.begin()

    def begin(self):
        self.setposition(STARTING_POSITION)

    def finish_line(self):
        if self.ycor() == FINISH_LINE_Y:
            return True
        else:
            return False

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def move_down(self):
        self.backward(MOVE_DISTANCE)
