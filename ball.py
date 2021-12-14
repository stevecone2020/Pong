from turtle import Turtle
import time


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.setposition(0, 0)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self, axis_to_bounce):
        self.move_speed *= 0.9
        if axis_to_bounce == "y":
            self.y_move *= -1
        elif axis_to_bounce == "x":
            self.x_move *= -1

    def reset_position(self):
        self.move_speed = 0.1
        self.goto(0, 0)
        self.bounce("x")