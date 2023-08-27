from turtle import Turtle, Screen
import heroes
import random


class Draw:
    def __init__(self):
        self.turtle = Turtle()
        self.turtle.shape("turtle")
        self.turtle.width(10)
        screen = self.turtle.screen
        self.screen = screen

    def square(self):
        for i in range(4):
            self.turtle.forward(100)
            self.turtle.left(90)

    def dashed_line(self, length=15, step_size=10):
        for _ in range(0, length):
            self.turtle.penup()
            self.turtle.forward(step_size)
            self.turtle.pendown()
            self.turtle.forward(step_size)

    def regular_shapes(self, one_side_len=100, speed=10):
        self.turtle.speed = speed
        for i in range(3, 30):
            turning_angle = 180 - ((i - 2) * 180) / i
            print(turning_angle)
            # self.turtle.color(self.random_color())
            self.turtle.pencolor(self.random_color())
            for _ in range(i):
                self.turtle.begin_fill()
                self.turtle.forward(one_side_len)
                self.turtle.left(turning_angle)
                self.turtle.end_fill()

    def random_color(self):
        r = random.random()
        g = random.random()
        b = random.random()
        return r, g, b

    def random_walk(self, one_walk_len=100, iterations=100):
        for _ in range(iterations):
            self.turtle.color(self.random_color())
            angle = random.choice([0, 90, 180, 270])
            self.turtle.left(angle)
            self.turtle.forward(one_walk_len)

    def spirograph(self, circles_count=20, radius = 80):
        self.turtle.width(5)
        for _ in range(circles_count):
            self.turtle.pencolor(self.random_color())
            self.turtle.circle(radius)
            self.turtle.left(360/circles_count)




draw = Draw()
draw.spirograph()
draw.screen.exitonclick()
