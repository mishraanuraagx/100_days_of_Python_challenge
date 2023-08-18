
print("Welcome to the tip calculator!")
bill = int(input("What was the total bill? $"))
tip = int(input("How much percentage of tip would you like to give? "))
people = int(input("How many people to split the bill? "))
amount_per_person = (bill + (tip*bill/100)) / (people)
print(f"Each person should pay: ${amount_per_person}")
