import random
import os
import art
import game_data

data = game_data.data

def welcome_screen():
    print(art.logo)


def vs_question():
    compare_A = random.choice(data)
    compare_B = random.choice(data)
    print(f"Compare A: {compare_A['name']}, {compare_A['description']}, from {compare_A['country']}")
    print(art.vs)
    print(f"Against B: {compare_B['name']}, {compare_B['description']}, from {compare_B['country']}")
    answer = input("Who has more followers? Type 'A' or 'B': ")

    if (answer.lower() == 'a' and int(compare_A["follower_count"]) > int(compare_B["follower_count"])) or  (answer.lower() == 'b' and int(compare_A["follower_count"]) < int(compare_B["follower_count"])):
        return True, compare_A, compare_B
    
    return False, compare_A, compare_B

def main():
    os.system('clc' if os.name =='nt' else 'clear')
    correct_answer = True
    welcome_screen()
    score = 0
    while correct_answer:
        correct_answer, A, B = vs_question()
        if correct_answer:
            score += 1
            os.system('clc' if os.name =='nt' else 'clear')
            print(art.logo)
            print(f"You are right. Current score: {score}")
        else:
            os.system('clc' if os.name =='nt' else 'clear')
            print(art.logo)
            print(f"Sorry, that's wrong. Final score: {score}")
        print(f"{A['name']} has {A['follower_count']}M followers whereas {B['name']} has {B['follower_count']}M\n")

    
    


main()


