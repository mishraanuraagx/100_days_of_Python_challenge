import random
import os


def print_status(guess_left):
    print(f"You have {guess_left} attempts remaining to guess the number.")


def welcome_message():
    print("Welcome to the number guessing game")
    number = random.randint(1,101)
    print("I'm thinking of a number between 1-100")
    difficulty = input("Choose a difficulty, type 'easy' or 'hard' : ")

    return number , difficulty


def print_diff_message(diff, message):
    if abs(diff) > 5:
        print("Too " + message)
    else:
        print("Closer but still " + message)


def main():
    number, difficulty = welcome_message()
    guess_left = 10 if difficulty.lower() == 'easy' else 5
    print_status(guess_left)
    while guess_left > 0:
        player_guess = int(input("Make a guess: "))
        if player_guess > number:
            guess_left -= 1
            print_diff_message(player_guess-number, "High!!!")
        elif player_guess < number:
            guess_left -= 1
            print_diff_message(player_guess-number, "Low!!!")
        else:
            print("You guess correctly!!!")
            break

        if guess_left == 0:
            print(f"You have failed to guess the number. The number was {number}")

        print_status(guess_left)


if __name__ == "__main__":
    main()
    
