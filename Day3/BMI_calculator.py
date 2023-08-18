print("Welcome to the BMI calculator v2.0")
age = float(input("Please tell us your age. "))
weight = float(input("Please tell us your weight in KG. "))
height = float(input("Please tell us your height in m. "))

bmi = weight/(height*height)

if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your bmi is {bmi}, you are normal weight.")
elif bmi < 30:
    print(f"Your bmi is {bmi}, you are overweight.")
elif bmi < 35:
    print(f"Your bmi is {bmi}, you are Obese.")
else:   
    print(f"Your bmi is {bmi}, you are clinically Obese")
