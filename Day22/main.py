from paddle import Paddle
from turtle import Screen
from scoreboard import Scoreboard
from ball import Ball
import constants
import time
import random

screen = Screen()
screen.setup(width=constants.GAME_WIDTH + 100, height=constants.GAME_HEIGHT + 100)
screen.bgcolor("black")
screen.title("My Ping-Ping Game")
screen.tracer(0)

# create objects
paddle = Paddle()
score_board = Scoreboard()
ball = Ball()

# score tracking
score_left = 0
score_right = 0

# key binding
screen.listen()
screen.onkey(paddle.left_up, "w")
screen.onkey(paddle.left_down, "s")
screen.onkey(paddle.right_up, "Up")
screen.onkey(paddle.right_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    # detect wall collision
    # upper wall
    angle_variance = random.randint(1, 5)
    if ball.ball.pos()[1] > constants.GAME_HEIGHT / 2 - 5:
        current_heading = ball.ball.heading() + angle_variance
        ball.ball.setheading(-current_heading)
    # lower wall
    elif ball.ball.pos()[1] < -constants.GAME_HEIGHT / 2 + 5:
        current_heading = ball.ball.heading() + angle_variance
        ball.ball.setheading(-current_heading)

    # Paddle collision
    # closer to left
    if ball.ball.pos()[0] < -constants.GAME_WIDTH / 2 + 5:
        for segment in paddle.paddle_left:
            if segment.distance(ball.ball.pos()) < 10:
                current_heading = ball.ball.heading() + angle_variance + 90
                ball.ball.setheading(current_heading)
                break
    # closer to right
    elif ball.ball.pos()[0] > constants.GAME_WIDTH / 2 - 5:
        for segment in paddle.paddle_right:
            if segment.distance(ball.ball.pos()) < 10:
                current_heading = ball.ball.heading() + angle_variance + 90
                ball.ball.setheading(current_heading)
                break
    # if ball crosses the left/right boundary, game over, assign-update score and reset the ball
    if ball.ball.pos()[0] < -constants.GAME_WIDTH / 2 - 20:
        time.sleep(0.5)
        score_right += 1
        score_board.update_score(score_left, score_right)
        ball.reset()
    elif ball.ball.pos()[0] > constants.GAME_WIDTH / 2 + 20:
        time.sleep(0.5)
        score_left += 1
        score_board.update_score(score_left, score_right)
        ball.reset()

    time.sleep(0.05)

screen.exitonclick()
