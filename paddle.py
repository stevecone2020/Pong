from turtle import Turtle, Screen


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")        # starts as a 20 by 20 square
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)        # stretches the square by these multiples
        self.setposition(position)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
        
    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
