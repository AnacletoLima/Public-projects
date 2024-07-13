#100DaysOfCode
#TheAppBrewery

from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_position, y_position):
        super().__init__()
        self.shape("square")
        self.right(90)
        self.setposition(x=x_position, y=y_position)
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()

    def move_up(self):
        self.backward(20)

    def move_down(self):
        self.forward(20)
