from turtle import Turtle
import constants
import random


class Car:
    def __init__(self):
        # create some random number of cars
        self.cars = []
        self.cars_speed = []
        self.unused_cars = []
        self.difficulty = 1
        self.create_cars()

    def reset(self):
        self.difficulty = 1



    def create_cars(self, random_pos=True, cars_number=10):
        # if random_pos == false, start the cars from right border
        for _ in range(cars_number):
            posx = random.randint(-constants.GAME_WIDTH / 2, constants.GAME_WIDTH / 2)
            posy = random.randint(-constants.GAME_HEIGHT / 2, constants.GAME_HEIGHT / 2)
            if len(self.unused_cars) > 0:
                car = self.unused_cars.pop(0)
            else:
                car = Turtle("car")
            car.penup()
            car.goto(posx, posy)
            car.color(random.choice(constants.CARS_COLOR_LIST))
            self.cars.append(car)
            self.cars_speed.append(random.randint(1,3))


    def move(self):
        pop_list = []
        for i in range(len(self.cars)):
            car:Turtle = self.cars.pop(0)
            speed:int = self.cars_speed.pop(0) + self.difficulty
            car.setx(car.pos()[0] - speed)
            # if car reached left side border
            if car.pos()[0] < -constants.GAME_WIDTH/2 - 20:
                car.reset()
                pop_list.append(i)
            else:
                self.cars.append(car)
                self.cars_speed.append(speed)


    def add_new_car(self):
        self.create_cars(cars_number=1)
        # set car to the right of the screen
        car = self.cars[-1]
        min_height = -constants.GAME_HEIGHT/2 + 15
        max_height = constants.GAME_HEIGHT/2 - 5
        car.setx(constants.GAME_WIDTH/2)
        car.sety((random.randint(min_height,max_height)//20)*20)

    def inc_difficulty(self):
        self.difficulty += 2
