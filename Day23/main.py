from car import Car
import constants
from turtle import Turtle, Screen
import time
import random
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.setup(width=constants.GAME_WIDTH + 200, height=constants.GAME_HEIGHT + 300)
screen.register_shape("car", ((-10, -20), (10, -20), (10, 20), (-10, 20)))

# car
car_controller = Car()
player = Player()
scoreboard = Scoreboard()

# screen binding
screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")
screen.onkey(player.right, "Right")
screen.onkey(player.left, "Left")
score = 0
game_over = False
while not game_over:
    car_controller.move()
    if random.randint(0, 10) > 5: car_controller.add_new_car()  # perform this only 30% of the time
    screen.update()

    # win condition
    if player.object.pos()[1] >= constants.GAME_HEIGHT / 2:
        scoreboard.level_complete()
        score += 1
        scoreboard.update_score(score)
        car_controller.inc_difficulty()
        player.reset()

    # loose condition
    for car in car_controller.cars:
        player_pos = player.object.pos()
        if abs(car.pos()[0] - player_pos[0]) < 35 and abs(car.pos()[1] - player_pos[1]) < 18:
            scoreboard.game_over()
            score = 0
            scoreboard.update_score(score)
            player.reset()
            car_controller.reset()
            break

    time.sleep(0.3)

screen.exitonclick()
