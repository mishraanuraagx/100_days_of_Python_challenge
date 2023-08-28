from turtle import Turtle, Screen
import constants
import random


class Ball(Turtle):
    def __init__(self):
        self.ball = Turtle("circle")
        self.reset()
        self.ball.color(constants.BALL_COLOR)
        self.ball.penup()

    def move(self):
        self.ball.forward(constants.BALL_SPEED)

    def reset(self):
        self.ball.goto((0, 0))
        self.ball.setheading(125 + random.randint(-10, 10))
