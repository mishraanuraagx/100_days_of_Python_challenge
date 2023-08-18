import random

action = input("Press Enter to flip a coin. ")
tails_counter = 0
heads_counter = 0
while action == '':
    random_int  = random.randint(0,1)
    if random_int == 1:
        print("Heads")
        heads_counter += 1
    else :
        print("Tails")
        tails_counter += 1

    print(f"# Heads = {heads_counter},  # Tails = {tails_counter} ")
    action = input("Flip again? (Press Enter) ")


