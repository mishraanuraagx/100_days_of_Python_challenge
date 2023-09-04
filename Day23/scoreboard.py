from turtle import Turtle
import constants
import time

class Scoreboard:
    def __init__(self):
        self.board_drawer = Turtle()
        self.board_drawer.penup()
        self.draw_board()

        self.score_printer = Turtle()
        self.score_printer.penup()
        self.score_printer.goto(0, constants.GAME_HEIGHT / 2 + 20)
        self.score_printer.pendown()
        self.score_printer.hideturtle()
        self.update_score()

        self.message_writer = Turtle()
        self.message_writer.penup()
        self.message_writer.goto(0, 0)
        self.message_writer.pendown()
        self.message_writer.hideturtle()

    def draw_board(self):
        self.board_drawer.goto(-constants.GAME_WIDTH / 2, -constants.GAME_HEIGHT / 2)
        self.board_drawer.pendown()
        self.board_drawer.color("black")
        self.board_drawer.goto(constants.GAME_WIDTH / 2, -constants.GAME_HEIGHT / 2)
        self.board_drawer.goto(constants.GAME_WIDTH / 2, constants.GAME_HEIGHT / 2)
        # draw finish line with green color
        self.board_drawer.color("green")
        self.board_drawer.goto(-constants.GAME_WIDTH / 2, constants.GAME_HEIGHT / 2)
        self.board_drawer.color("black")
        self.board_drawer.goto(-constants.GAME_WIDTH / 2, -constants.GAME_HEIGHT / 2)
        self.board_drawer.pendown()
        self.board_drawer.hideturtle()

    def update_score(self, score=0):
        self.score_printer.clear()
        self.score_printer.color("black")
        self.score_printer.write(f"{score}", align="center", font=("Arial", 20, "bold"))

    def game_over(self):
        self.message_writer.color("red")
        self.message_writer.write("GAME OVER!", align="center", font=("Arial", 20, "bold"))
        time.sleep(1)
        self.message_writer.clear()

    def level_complete(self):
        self.message_writer.color("green")
        self.message_writer.write("Level Complete!", align="center", font=("Arial", 20, "bold"))
        time.sleep(1)
        self.message_writer.clear()
