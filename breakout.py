import time
import random

from turtle import Screen
from paddle import Paddle
from ball import Ball
from bricks import Brick
from scoreboard import Scoreboard

BRICK_COLORS = iter(["yellow", "green", "orange", "red"])
brick_color = next(BRICK_COLORS)

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout")
screen.tracer(0)

screen.listen()

paddle = Paddle()
ball = Ball()
scoreboard = Scoreboard()
wall = []
score = 0
turns = 3
hits = 0
orange_wall_whole = True
red_wall_whole = True

# build the wall of bricks
for row in range(0, 8):
    if row % 2 == 0 and row != 0:
        try:
            brick_color = next(BRICK_COLORS)
        except StopIteration:
            pass
    for i in range(40):
        wall.append(Brick(brick_color,
                          positions=(-390 + (i * 20), 100 + row * 20)))

screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")

game_is_on = True

while game_is_on:
    print(ball.x_speed, ball.y_speed)
    time.sleep(0.001)
    screen.update()
    scoreboard.clear()
    scoreboard.write(f"turns: {turns} | points {score}")
    ball.move()

    # detect collision with the paddle
    if ball.distance(paddle) < 45 and ball.ycor() < -260:
        if ball.y_speed < 0:
            ball.bounce("y", obj=paddle)

    # detect collision with the top
    elif ball.ycor() > 280:
        paddle.shapesize(stretch_len=3)
        ball.bounce("y")

    # detect collision with the bottom
    elif ball.ycor() < -280:
        turns -= 1
        ball.setpos(0, 0)
        ball.x_speed = random.choice([-3.5, 3.5])
        ball.y_speed = -3.5
        hits = 0

    # detect collision with the side walls
    elif ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce("x")

    # detect collision with the bricks
    for brick in wall:
        if ball.distance(brick) < 15:
            ball.bounce("y", obj=brick)
            brick.goto(1000, 1000)
            hits += 1
            if hits == 4 or hits == 12:
                ball.y_speed -= 1
            if brick.color()[1] == "yellow":
                score += 1
            elif brick.color()[1] == "green":
                score += 3
            elif brick.color()[1] == "orange":
                score += 5
                if orange_wall_whole:
                    ball.y_speed -= 1
                    orange_wall_whole = False
            else:
                score += 7
                if red_wall_whole:
                    ball.y_speed -= 1
                    red_wall_whole = False
            break
    game_is_on = turns


screen.exitonclick()
