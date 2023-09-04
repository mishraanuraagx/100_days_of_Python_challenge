import turtle as td_module
import random
import time


class Snake:
    def __init__(self):
        self.scoreboard = None
        self.high_score = 0
        self.speed = 0.3
        self.read_save_file()
        self.auto_move = False
        self.food = None
        self.direction = None
        self.pos = []
        self.snake = td_module.Turtle()
        self.screen = td_module.Screen()
        self.width = 600
        self.height = 600
        self.box_width = 20
        self.initial_size = 3
        self.score = 0
        self.screen.tracer(0)
        self.screen.setup(width=self.width+100, height=self.height+100)
        self.screen.register_shape("box", (
            (-self.box_width / 2, -self.box_width / 2), (-self.box_width / 2, self.box_width / 2),
            (self.box_width / 2, self.box_width / 2),
            (self.box_width / 2, -self.box_width / 2)))
        self.instruction_drawer = None
        self.reset()
        self.key_bind()

    def read_save_file(self):
        with open('save.file', mode='r') as file:
            content = file.readlines()
            print(content)
            self.high_score = int(content[0].replace("\n","").split("=")[1])
            self.speed = float(content[1].replace("\n","").split("=")[1])

    def get_score(self):
        return len(self.snake) - self.initial_size

    def update_score(self):
        if self.scoreboard == None:
            self.scoreboard = td_module.Turtle()
            self.scoreboard.penup()
            self.scoreboard.sety(self.height / 2)
            self.scoreboard.hideturtle()
        self.scoreboard.clear()
        self.scoreboard.write(f"Score: {self.get_score()}, High Socre: {self.high_score}", align='center', font=("Arial", 16, "normal"))

    def create_starter_snake(self):
        x = 0
        y = 0
        for i in range(self.initial_size):
            self.snake.append(self.create_snake_shape(x + i * self.box_width, y))

    def create_snake_shape(self, posx=0, posy=0):
        box = td_module.Turtle()
        box.hideturtle()
        box.shape("box")
        box.color("black")
        box.penup()
        box.setx(posx)
        box.sety(posy)
        box.showturtle()
        return box

    def key_bind(self):
        self.screen.listen()
        self.screen.onkey(self.start_stop, " ")
        self.screen.onkey(self.left, "Left")
        self.screen.onkey(self.right, "Right")
        self.screen.onkey(self.up, "Up")
        self.screen.onkey(self.down, "Down")
        self.screen.onscreenclick(None)

    # def do_nothing(self):
    #     print("here")
    #     pass

    def start_stop(self):
        self.instruction_drawer.clear()
        self.auto_move = not self.auto_move
        if self.auto_move:
            self.move()

    def move(self):
        while self.auto_move:
            self.screen.update()
            time.sleep(self.speed)
            new_posx, new_posy = self.get_next_pos()

            food_in_front = self.something_in_front(self.food.pos()[0], self.food.pos()[1], new_posx, new_posy)
            snake_part = None

            if self.collision_with_self(new_posx, new_posy) or self.collision_with_wall(new_posx, new_posy):
                self.auto_move = False
                # show message and score
                time.sleep(2)
                self.write_save_file()
                self.reset()
                break

            if not food_in_front:
                snake_part: td_module.Turtle = self.snake.pop(0)
                snake_part.hideturtle()
                snake_part.setx(new_posx)
                snake_part.sety(new_posy)
                snake_part.showturtle()
                # time.sleep(0.2)
            else:
                snake_part: td_module.Turtle = self.create_snake_shape(new_posx, new_posy)
                self.food.hideturtle()
                self.food = self.place_food()
                self.update_score()

            self.snake.append(snake_part)

    def draw_boundary(self):
        boundary = td_module.Turtle()
        boundary.hideturtle()
        boundary.penup()
        # move to the bottom-left corner
        boundary.setx(-self.width / 2)
        boundary.sety(-self.height / 2)

        boundary.pendown()
        # move to botton-right corner
        boundary.setx(self.width / 2)
        boundary.sety(-self.height / 2)
        # move to top-right corner
        boundary.setx(self.width / 2)
        boundary.sety(self.height / 2)
        # move to top-left corner
        boundary.setx(-self.width / 2)
        boundary.sety(self.height / 2)
        # move to bottom-left corner
        boundary.setx(-self.width / 2)
        boundary.sety(-self.height / 2)
        boundary.penup()

    def reset(self):
        if self.scoreboard:
            self.scoreboard.clear()
            self.scoreboard = None
        self.screen.reset()
        for turtle in td_module.turtles():
            turtle.hideturtle()
        self.snake: [td_module.Turtle] = []
        self.create_starter_snake()
        # default [up, down, right, left]
        self.direction = 'right'
        self.food = self.place_food()
        self.auto_move = False
        self.update_score()
        self.draw_boundary()
        self.score = self.get_score()
        self.print_instruction()
        self.screen.update()

    def write_save_file(self):
        with open('save.file', mode='w') as file:
            if self.get_score() > self.high_score: self.high_score = self.get_score()
            file.write(f'high_score = {self.high_score} \n snake_speed = {self.speed}')

    def get_next_pos(self):
        first_box = self.snake[0]
        last_snake = self.snake[-1]
        posx = 0
        posy = 0
        if self.direction == 'right':
            # move right
            posx = last_snake.pos()[0] + self.box_width
            posy = last_snake.pos()[1]
        elif self.direction == 'left':
            # move left
            posx = last_snake.pos()[0] - self.box_width
            posy = last_snake.pos()[1]
        elif self.direction == 'up':
            # move up
            posx = last_snake.pos()[0]
            posy = last_snake.pos()[1] + self.box_width
        elif self.direction == 'down':
            # move down
            posx = last_snake.pos()[0]
            posy = last_snake.pos()[1] - self.box_width
        return posx, posy

    def left(self):
        print("left is pressed")
        if self.direction != 'right':
            self.direction = 'left'

    def right(self):
        print("right is pressed")
        if self.direction != 'left':
            self.direction = 'right'

    def up(self):
        print("up is pressed")
        if self.direction != 'down':
            self.direction = 'up'

    def down(self):
        print("down is pressed")
        if self.direction != 'up':
            self.direction = 'down'

    def place_food(self):
        width = self.width
        height = self.height
        pos_found = False
        food = None
        while not pos_found:
            # get posx and posy that a food of snake size can be placed there, should be a pixel pos that the snake box takes
            # making sure it is exactly divisible by box_width
            posx = int(random.randint(self.box_width, width - self.box_width) // self.box_width) * self.box_width
            posy = int(random.randint(self.box_width, height - self.box_width) // self.box_width) * self.box_width
            posx = posx - width / 2
            posy = posy - height / 2
            print(f"{posx}, {posy}")
            # check if snake is already there
            pos_found = self.coordinate_free(posx, posy, self.snake)
            # position is generated within snake body
            if pos_found:
                food = self.create_snake_shape(posx, posy)
                pos_found = True

        food.color("blue")
        return food

    def coordinate_free(self, posx, posy, parts):
        for part in parts:
            if (part.pos()[0] + self.box_width > posx) and (part.pos()[0] - self.box_width < posx) and (
                    part.pos()[1] + self.box_width > posy) and (part.pos()[1] - self.box_width < posy):
                return False
        return True

    def something_in_front(self, food_posx, food_posy, posx, posy):
        if (posx + self.box_width > food_posx) and (posx - self.box_width < food_posx) and (
                posy + self.box_width > food_posy) and (posy - self.box_width < food_posy):
            return True
        return False

    def collision_with_self(self, new_posx, new_posy):
        # check whether new coordinate update means collision
        for part in self.snake[:-2]:
            if self.something_in_front(part.pos()[0], part.pos()[1], new_posx, new_posy):
                return True

        return False

    def collision_with_wall(self, new_posx, new_posy):
        # right wall or top
        if new_posx >= self.width / 2 or new_posx <= -self.width / 2 or new_posy >= self.height / 2 or new_posy <= -self.height / 2:
            return True
        return False


    def print_instruction(self):
        if self.instruction_drawer == None:
            self.instruction_drawer = td_module.Turtle()
        self.instruction_drawer.penup()
        self.instruction_drawer.color("black")
        self.instruction_drawer.hideturtle()
        self.instruction_drawer.clear()
        self.instruction_drawer.goto(0,40)
        self.instruction_drawer.write(f"Press Space to Start.",align='center', font=("Arial", 16, "normal"))


snake = Snake()
snake.screen.mainloop()
