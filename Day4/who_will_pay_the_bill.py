import random

names = input("Give me everybody's name, separated by comma_space ', ' ")
names = names.split(", ")

print(f"Just to be sure these are all the names, {names}")
person = random.choice(names)
print(f"{person} is going to buy the meal today!")
