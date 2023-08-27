import random
import turtle as turtle_module

rgb_colors = [(250, 245, 240), (153, 91, 49), (209, 156, 107), (42, 111, 146), (60, 116, 75), (199, 157, 31)]

turtle_module.colormode(255)
turtle = turtle_module.Turtle()
screen = turtle.screen
turtle.shape("turtle")
painting_width = 500
dots_per_line = 10
dot_size = 20
movement_per_tick = painting_width/dots_per_line
# position itself to an ideal position to start the drawing
turtle.penup()
turtle.left(180)
turtle.forward(500)
turtle.left(90)
turtle.forward(300)
turtle.left(90)

for _ in range(dots_per_line):
    for _ in range(dots_per_line):
        # draw a dot and move forward
        turtle.pendown()
        turtle.dot(dot_size, random.choice(rgb_colors))
        turtle.penup()
        turtle.forward(movement_per_tick)

    # reset itself at the start of the next line
    turtle.penup()
    turtle.left(90)
    turtle.forward(movement_per_tick)
    turtle.left(90)
    turtle.forward(painting_width)
    turtle.left(180)

screen.exitonclick()