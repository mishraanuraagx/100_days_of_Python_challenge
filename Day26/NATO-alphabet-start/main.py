student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    print(f"{key}: {value}")

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print("Accessing row: " + str(student_data_frame.iloc[index]))
    print("Student " + row.student)
    print("Score :" + str(row.score))

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
nato_alpha_dataset = pandas.read_csv("nato_phonetic_alphabet.csv").set_index("letter")
nato_dict = nato_alpha_dataset.code.to_dict()

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
continue_prompting = True
while continue_prompting:
    name = input("Please insert the name for nato alphabet : ").lower()
    if name == "exit" or '':
        continue_prompting = False
        continue
    nato_list = [nato_dict[char.upper()] if char.upper() in nato_dict else char for char in list(name)]
    print(nato_list)
    print()

