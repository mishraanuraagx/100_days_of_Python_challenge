import random

rock = """
rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
paper
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
scissors
_______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


computer_won = 0
player_won = 0
action_list = [rock, paper, scissors]
action = int(input("What do you choose? type 0 - Rock, 1- Paper, 2 - Scissors. \n"))

while action >=0 and action <3:
    computer_choice = random.choice([0,1,2])
    print(f"Computer chose \n{action_list[computer_choice]}\n")            
    print(f"You chose \n{action_list[action]}\n")
    
    if action == computer_choice:
        print("DRAW!")
    elif (action == 0 and computer_choice == 2) or (action == 1 and computer_choice == 0) or (action == 2 and computer_choice == 1):
        print("You win!")
        player_won += 1
    else:
        print("You lost!")
        computer_won += 1
    print(f"Computer - {computer_won} , Player - {player_won}")
    action = int(input("What do you choose? type 0 - Rock, 1- Paper, 2 - Scissors. \n"))


