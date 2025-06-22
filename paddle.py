from turtle import Turtle

MOVE_DISTANCE = 10
class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(5, 1)
        self.penup()
        self.goto(position)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_x = self.ycor() - 20
        self.goto(self.xcor(), new_x)