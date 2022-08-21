import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout")
screen.tracer(0)

screen.listen()

paddle = Paddle()
ball = Ball()

screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")

game_is_on = True

while game_is_on:

    time.sleep(0.01)
    screen.update()
    ball.move()
    if ball.ycor() > 280: #or ball.ycor() < -280:
        ball.bounce("y")
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce("x")
    if ball.distance(paddle) < (20 + paddle.shapesize()[1]):
        print(ball.distance(paddle))
        print(paddle.shapesize())
        ball.bounce("y")

screen.exitonclick()
