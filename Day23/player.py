from turtle import Turtle, Screen
import constants


class Player:
    def __init__(self):
        self.object = Turtle("turtle")
        self.object.setheading(90)
        self.object.penup()
        self.object.color(constants.TURTLE_COLOR)
        self.object.goto(-constants.GAME_WIDTH / 2, -constants.GAME_HEIGHT/2 - 20)
        self.screen = Screen()

    def up(self):
        self.object.sety(self.object.pos()[1] + 10)
        self.screen.update()


    def down(self):
        self.object.sety(self.object.pos()[1] - 10)
        self.screen.update()

    def left(self):
        self.object.setx(self.object.pos()[0] - 10)
        self.screen.update()

    def right(self):
        self.object.setx(self.object.pos()[0] + 10)
        self.screen.update()
