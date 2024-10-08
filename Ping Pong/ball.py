from turtle import Turtle
import time


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 3
        self.y_move = 3
        self.move_speed = 1

    def move(self):
        new_x = self.xcor() + self.x_move*self.move_speed
        new_y = self.ycor() + self.y_move*self.move_speed
        time.sleep(0.01)
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 1.01

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 1
        self.bounce_x()
