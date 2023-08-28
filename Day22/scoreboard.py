from turtle import Turtle
import constants


class Scoreboard(Turtle):
    def __init__(self):
        posx = 0
        posy = constants.GAME_HEIGHT / 2 + 20
        self.score_card = Turtle()
        self.boundary = Turtle()

        self.score_card.penup()
        self.draw_boundary()
        self.score_card.color("white")
        self.score_card.hideturtle()
        self.score_card.goto((posx, posy))
        self.update_score()

    def update_score(self, score_left=0, score_right=0):
        self.score_card.clear()
        self.score_card.write(f"{score_left} : {score_right}", align="center", font=("Arial", 20, "bold"))

    def draw_boundary(self):
        self.boundary.penup()
        self.boundary.pencolor("white")
        self.boundary.goto((-constants.GAME_WIDTH / 2, -constants.GAME_HEIGHT / 2))
        print("here")
        self.boundary.pendown()
        self.boundary.goto((constants.GAME_WIDTH / 2, -constants.GAME_HEIGHT / 2))
        self.boundary.goto((constants.GAME_WIDTH / 2, constants.GAME_HEIGHT / 2))
        self.boundary.goto((-constants.GAME_WIDTH / 2, constants.GAME_HEIGHT / 2))
        self.boundary.goto((-constants.GAME_WIDTH / 2, -constants.GAME_HEIGHT / 2))
        self.boundary.penup()
        self.boundary.hideturtle()
        # draw separator
        self.boundary.goto((0, -constants.GAME_HEIGHT / 2))
        self.boundary.setheading(90)
        while self.boundary.pos()[1] < constants.GAME_HEIGHT / 2 - 10:
            self.boundary.forward(10)
            self.boundary.pendown()
            self.boundary.forward(10)
            self.boundary.penup()
