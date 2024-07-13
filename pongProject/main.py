from turtle import Screen
from ball import Ball
from movement import Movement
from scoreboard import Scoreboard


def exit_game():
    global playing
    playing = False


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")

ball = Ball()
tick = Movement()
scoreboard = Scoreboard()
tick.tick()

playing = True
while playing:
    screen.update()
    ball.move()
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
    if 340 >= ball.xcor() >= 330 and ball.distance(tick.r_paddle) <= 61:
        ball.bounce_x()
        ball.setposition(329, ball.ycor())
        ball.increase_speed_right()
    elif ball.xcor() > 340 and ball.distance(tick.r_paddle) <= 61:
        ball.bounce_y()
    if -340 <= ball.xcor() <= -330 and ball.distance(tick.l_paddle) <= 61:
        ball.bounce_x()
        ball.setposition(-329, ball.ycor())
        ball.increase_speed_left()
    elif ball.xcor() < -340 and ball.distance(tick.l_paddle) <= 61:
        ball.bounce_y()
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.l_point()
        ball.default_speed()
    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_point()
        ball.default_speed()
    screen.onkeypress(exit_game, "space")

screen.bye()
