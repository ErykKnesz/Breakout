from turtle import Turtle


class Brick(Turtle):

    def __init__(self, color, positions, length=0.952380952380952):
        super().__init__()
        self.shape("square")
        self.fillcolor(color)
        self.pencolor("grey")
        self.shapesize(stretch_len=length)
        self.penup()
        self.setpos(positions)