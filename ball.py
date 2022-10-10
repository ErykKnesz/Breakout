from turtle import Turtle

START_SPEED_Y = -3.5
START_SPEED_X = 3.5

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_speed = START_SPEED_X
        self.y_speed = START_SPEED_Y

    def move(self):
        new_x = self.xcor() + self.x_speed
        new_y = self.ycor() + self.y_speed
        self.goto(new_x, new_y)

    def bounce(self, mode, obj=None):
        if mode == "y":
            self.y_speed *= -1
            if obj is not None:
                if self.xcor() < obj.xcor():
                    self.x_speed *= -1

        else:
            self.x_speed *= -1

