from turtle import Turtle

START_SPEED = 1.5


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_speed = START_SPEED
        self.y_speed = START_SPEED

    def move(self):
        new_x = self.xcor() + self.x_speed
        new_y = self.ycor() + self.y_speed
        self.goto(new_x, new_y)

    def bounce(self, mode):
        if mode == "y":
            self.y_speed *= -1
        else:
            self.x_speed *= -1

