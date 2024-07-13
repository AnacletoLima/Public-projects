import time
from turtle import Screen
from cross_turtle import CrossTurtle
from cars import Cars
from screen_text import ScreenText

screen = Screen()
screen.setup(600, 600)
screen.title("Turtle Crossing")
screen.tracer(0)
screen.listen()

text = ScreenText()
turtle = CrossTurtle()
cars = Cars()
game_is_on = True

screen.onkey(turtle.move_up, "Up")
screen.onkey(turtle.move_down, "Down")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move()
    for car in cars.cars_list:
        if car.distance(turtle) < 20:
            game_is_on = False
            text.game_over()
    if turtle.finish_line():
        turtle.begin()
        cars.level_up()
        text.next_level()

screen.exitonclick()
