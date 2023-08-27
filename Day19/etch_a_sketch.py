import turtle as td_module

turtle = td_module.Turtle()
fd = turtle.forward
lf = turtle.left
screen = turtle.screen


class Timothy:
    auto_run = False

    def up(self):    fd(50)

    def down(self):  fd(-50)

    def left(self):  lf(5)

    def right(self): lf(-5)

    def clear(self):
        turtle.clear()
        turtle.penup()
        turtle.home()
        turtle.pendown()

    def auto_forward(self):
        self.auto_run = True
        turtle.speed(1)
        while self.auto_run:
            fd(10)

    def stop_auto_forward(self):
        self.auto_run = False

    def run(self):
        screen.listen()
        screen.onkey(self.up, "Up")
        screen.onkey(self.down, "Down")
        screen.onkeypress(self.left, "Left")
        screen.onkeypress(self.right, "Right")
        screen.onkey(self.auto_forward, "a")
        screen.onkey(self.stop_auto_forward, "s")
        screen.onkey(self.clear, "c")
        screen.exitonclick()



Timothy().run()