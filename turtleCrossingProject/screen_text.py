#100DaysOfCode
#TheAppBrewery

from turtle import Turtle

FONT = ('Arial', 15, 'normal')


class ScreenText(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.setposition(-270, 260)
        self.level = 1
        self.text_level()

    def text_level(self):
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def next_level(self):
        self.clear()
        self.level += 1
        self.text_level()

    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
