from turtle import Turtle, Screen
import constants


class Player:
    def __init__(self):
        self.object = Turtle("turtle")
        self.object.setheading(90)
        self.object.penup()
        self.object.color(constants.TURTLE_COLOR)
        self.object.goto(0, -constants.GAME_HEIGHT/2 - 20)
        self.screen = Screen()

    def reset(self):
        self.object.goto(0, -constants.GAME_HEIGHT/2 - 20)

    def up(self):
        if self.object.pos()[1] < constants.GAME_HEIGHT/2 + 15:
            self.object.sety(self.object.pos()[1] + constants.TURTLE_SPEED)
            self.screen.update()

    def down(self):
        if self.object.pos()[1] > -constants.GAME_HEIGHT/2 - 15:
            self.object.sety(self.object.pos()[1] - constants.TURTLE_SPEED)
            self.screen.update()

    def left(self):
        if self.object.pos()[0] > -constants.GAME_WIDTH/2:
            self.object.setx(self.object.pos()[0] - constants.TURTLE_SPEED)
            self.screen.update()

    def right(self):
        if self.object.pos()[0] < constants.GAME_WIDTH/2:
            self.object.setx(self.object.pos()[0] + constants.TURTLE_SPEED)
            self.screen.update()
