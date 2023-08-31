from car import Car
import constants
from turtle import Turtle, Screen
import time
from player import Player

screen = Screen()
screen.tracer(0)
screen.setup(width=constants.GAME_WIDTH + 200, height=constants.GAME_HEIGHT + 300)
screen.register_shape("car", ((-20, -40), (20, -40), (20, 40), (-20, 40)))

# car
car = Car()
player = Player()

# screen binding
screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")
screen.onkey(player.right, "Right")
screen.onkey(player.left, "Left")

game_over = False
while not game_over:
    car.move()
    car.add_new_car()
    screen.update()
    time.sleep(0.5)

screen.exitonclick()
