print("Welcome to the Love calculator!")

name1 = input("What is your name? ")
name2 = input("What is their name? ")

combined_names = name1.lower() + " " + name2.lower()

# calculate the number of times the letters of the word 'true' comes in both the names
true_count = 0
true_count += combined_names.count("t")
true_count += combined_names.count("r")
true_count += combined_names.count("u")
true_count += combined_names.count("e")
# calculate the number of times the letters of the word 'love' comes in both the names
love_count = 0
love_count += combined_names.count("l")
love_count += combined_names.count("o")
love_count += combined_names.count("v")
love_count += combined_names.count("e")

final_score = true_count*10 + love_count
if (final_score >= 90) or (final_score <= 10) :
    print(f"Your score is {final_score}, you go together like coke and mentos.")
else:
    print(f"Your score is {final_score}, you are alright together.")
