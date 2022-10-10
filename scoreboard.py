from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-390, -290)
        self.hideturtle()
        self.pencolor("pink")
