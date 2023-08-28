from turtle import Turtle, Screen
import constants


class Paddle(Turtle):
    def __init__(self):
        self.canvas_width = constants.GAME_WIDTH
        self.canvas_height = constants.GAME_HEIGHT
        # create left paddle
        self.paddle_left: [Turtle] = []
        self.create_paddle('left')

        # create right paddle
        self.paddle_right: [Turtle] = []
        self.create_paddle('right')

    def create_paddle(self, side):
        for i in range(constants.PADDLE_LENGTH):
            segment = Turtle("square")
            segment.penup()
            if side == 'left':
                segment.color(constants.PADDLE_LEFT_COLOR)
                segment.goto(-300, (-constants.PADDLE_LENGTH + i) * 20)
                self.paddle_left.append(segment)
            else:
                segment.color(constants.PADDLE_RIGHT_COLOR)
                segment.goto(300, (-constants.PADDLE_LENGTH + i) * 20)
                self.paddle_right.append(segment)

    def left_up(self):
        if self.paddle_left[-1].pos()[1] <= constants.GAME_HEIGHT / 2 - 20:
            for segment in self.paddle_left:
                segment.sety(segment.pos()[1] + 20)

    def left_down(self):
        if self.paddle_left[0].pos()[1] > -constants.GAME_HEIGHT / 2 - 20:
            for segment in self.paddle_left:
                segment.sety(segment.pos()[1] - 20)

    def right_up(self):
        if self.paddle_right[-1].pos()[1] < constants.GAME_HEIGHT / 2 - 20:
            for segment in self.paddle_right:
                segment.sety(segment.pos()[1] + 20)

    def right_down(self):
        if self.paddle_right[0].pos()[1] > -constants.GAME_HEIGHT / 2 - 20:
            for segment in self.paddle_right:
                segment.sety(segment.pos()[1] - 20)
