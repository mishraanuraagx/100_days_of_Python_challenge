import turtle as td_module
import random


class Race:
    def __init__(self):
        # create 10 turtle racers
        self.racers = []
        spacing = 50
        self.screen = td_module.Screen()
        self.screen.setup(width=500, height=800)
        self.y_start = -180
        colors = ["red", "green", "black", "blue", "pink", "purple", "skyblue", "violet", "tomato", "gold"]
        for i in range(len(colors)):
            turtle = td_module.Turtle()
            turtle.shape("turtle")
            turtle.penup()
            turtle.color(colors[i])
            turtle.setx(-200)
            turtle.sety(self.y_start + i * spacing)
            self.racers.append(turtle)
        self.user_bet, self.rig = self.bet()
        self.draw_lines()

    def draw_lines(self):
        # draw start line
        liner = td_module.Turtle()
        liner.shape("turtle")
        liner.penup()
        liner.color("black")
        liner.setx(-200)
        liner.sety(self.y_start)
        liner.pendown()
        liner.left(90)
        liner.forward(500)

        # draw finish line
        liner.penup()
        liner.sety(self.y_start)
        liner.setx(200)
        liner.pendown()
        liner.forward(500)

    def bet(self):
        user_bet = self.screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
        rig = self.screen.textinput(title="Pssssss....", prompt="Do you want me to rig the race? yes/no: ")
        print(f"User Bet: {user_bet}")
        return user_bet, rig

    def race(self):
        stop = False
        while not stop:
            for turtle in self.racers:
                distance_per_tick = random.randint(4, 6)
                # rigging the race
                if turtle.color()[0].lower() == self.user_bet.lower() and self.rig.lower() == 'yes':
                    # making sure it's not obvious
                    distance_per_tick = random.randint(5, 6)
                turtle.forward(distance_per_tick)
                if turtle.pos()[0] >= 200:
                    stop = True

        # check the winner
        winner: td_module.Turtle = self.racers[0]
        for racer in self.racers:
            if winner.pos()[0] < racer.pos()[0]:
                winner = racer

        print(f"Race is over. {winner.color()[0].upper()} won the race!")
        if self.user_bet.lower() == winner.color()[0].lower():
            print("You won the bet!")
        else:
            print("You lost the bet!")




race = Race()
race.race()
race.screen.exitonclick()
