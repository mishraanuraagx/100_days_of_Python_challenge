
import random

wordlist = ["sugarcane", "apple", "pineapple"]

print("Welcome to the Hangman game.")


health = 7
word = random.choice(wordlist)
guess_list = ["_" for _ in range(len(word))]
guess = " ".join(guess_list)

char_guessed_list = []

while (health > 0 and "_" in guess ):
    print(f"Word: {guess}    Health: {health}")
    char_guess = input("Guess a letter.\n")[0]
    if char_guess not in char_guessed_list:
        char_guessed_list.append(char_guess);
        if char_guess in word:
            print("Found one!")
            for i in range(len(word)):
                if word[i] == char_guess:
                    guess_list[i] = char_guess
        else:
            print("Bad guess. Try again.")
            health -= 1

    guess = " ".join(guess_list)

if (health == 0):
    print(f"You couldn't guess the word, the word was {word}")
else:
    print(
        f"Perfect! You were able to guess the word: {word} with {health} health left.")
