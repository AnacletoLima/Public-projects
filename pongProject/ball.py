from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 0.2
        self.y_move = 0.2

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def default_speed(self):
        self.x_move = 0.2
        self.y_move = 0.2

    def increase_speed_left(self):
        self.x_move += 0.1
        self.y_move += 0.1

    def increase_speed_right(self):
        self.x_move -= 0.1
        self.y_move -= 0.1

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.setposition(0, 0)
        self.bounce_x()
