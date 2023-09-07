import pandas as pd
from turtle import Turtle, Screen

data = pd.read_csv("50_states.csv")
player_tut = Turtle()
player_tut.hideturtle()
player_tut.penup()

screen = Screen()
screen.bgpic("blank_states_img.gif")

correct_answers = 0
states_count = len(data.state)
while correct_answers < states_count:
    left_to_guess = states_count - correct_answers
    player_input = screen.textinput(f"States left to guess: {states_count}", "Name the next possible state")
    if player_input == "solve":
        for index in data.index:
            # draw
            player_tut.goto(data.iloc[index].x, data.iloc[index].y)
            player_tut.write(f"{data.iloc[index].state}", align="center", font=("Arial", 10, "bold"))
            data.drop(index)
        break

    value_found = data[data.state.str.lower() == player_input]
    if not value_found.empty:
        # draw
        index = value_found.index.to_list()[0]
        player_tut.goto(data.iloc[index].x, data.iloc[index].y)
        player_tut.write(f"{data.iloc[index].state}", align="center", font=("Arial", 10, "bold"))
        data.drop(index)
        correct_answers += 1
    # exit the game
    elif player_input == 'exit':
        break

screen.exitonclick()
