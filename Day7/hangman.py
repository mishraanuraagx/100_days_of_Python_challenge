
import random
import os
import hangman_art

words = []

def read_words_from_file():
    with open("wordlist.txt", 'r') as f:
        words = f.readlines()
    return words

words = read_words_from_file()

print("Welcome to the Hangman game.")

# health 0 means game over = 7th mistake
health = 6
word = random.choice(words)
word = word.replace('\n','')
# to show all the position of alphabets that player has correctly guessed
guess_list = ["_" for _ in range(len(word))]

char_guessed_list = []

def clear_screen():
    # Call clear screen command based on the OS
    os.system('cls' if os.name=='nt' else 'clear')
    

def print_status(curr_health):
    # Show the user number of position left to guess and health
    print(hangman_art.HANGMAN_LOGO)
    print(hangman_art.HANGMAN_ART[curr_health])
    print(" Current status :\n Word: " + " ".join(guess_list)  + f"  Health: {health}")
    print(f"Letters Guessed : {sorted(char_guessed_list)}")
        

while (health > 0 and "_" in guess_list ):
    clear_screen()
    # The ASCII art is 0-6 index
    print_status(health)

    # ask the player to guess a letter
    char_guess = input("Guess a letter. ")[0].lower()

    # Only go throw the flow if the player has guessed the alphabet for the first time.
    if char_guess not in char_guessed_list:
        char_guessed_list.append(char_guess);
        if char_guess in word:
            # adding health back if the player guess is correct, else the game gets very hard based on the word length
            if health < 6: health += 1

            # good guess
            print("Found one!")
            for i in range(len(word)):
                if word[i] == char_guess:
                    guess_list[i] = char_guess
        else:
            # wrong guess
            print("Bad guess. Try again.")
            health -= 1
            


clear_screen()
print_status(health)
if (health == 0):
    print(f"\n\nYou couldn't guess the word, the word was '{word}'")
else:
    print(
        f"Perfect! You were able to guess the word: '{word}' with {health} health left.")
