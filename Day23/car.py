from turtle import Turtle
import constants
import random


class Car:
    def __init__(self):
        # create some random number of cars
        self.cars = []
        self.cars_speed = []
        self.difficulty = constants.DIFFICULTY['easy']
        self.create_cars()



    def create_cars(self, random_pos=True, cars_number=10):
        # if random_pos == false, start the cars from right border

        for _ in range(cars_number):
            posx = random.randint(-constants.GAME_WIDTH / 2, constants.GAME_WIDTH / 2)
            posy = random.randint(-constants.GAME_HEIGHT / 2, constants.GAME_HEIGHT / 2)
            car = Turtle("car")
            car.penup()
            car.goto(posx, posy)
            car.color(random.choice(constants.CARS_COLOR_LIST))
            self.cars.append(car)
            self.cars_speed.append(random.randint(self.difficulty, self.difficulty+3))


    def move(self):
        for i in range(len(self.cars)):
            car:Turtle = self.cars[i]
            speed:int = self.cars_speed[i]
            car.setx(car.pos()[0] - speed*5)

    def add_new_car(self):
        self.create_cars(cars_number=1)
        # set car to the right of the screen
        car = self.cars[-1]
        min_height = -constants.GAME_HEIGHT/2
        max_height = constants.GAME_HEIGHT/2
        car.setx(constants.GAME_WIDTH/2)
        car.sety(random.randint(min_height,max_height))
