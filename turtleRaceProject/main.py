#100DaysOfCode
#TheAppBrewery

import turtle
from random import randint


def create_turtle(name, turtle_color, y_coordinate):
    name = turtle.Turtle(shape="turtle")
    name.color(turtle_color)
    name.penup()
    name.goto(x=-230, y=y_coordinate)
    all_turtles.append(name)


is_race_on = False
screen = turtle.Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
index = 0
y = -100

for color in colors:
    create_turtle(color, colors[index], y)
    index += 1
    y += 40

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_distance = randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
