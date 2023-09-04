

email_content:str = ""
names_list = []
with open('./Input/Letters/starting_letter.txt', mode='r') as file:
    email_content = file.read()

with open('./Input/Names/invited_names.txt', mode='r') as file:
    content = file.readlines()
    for name in content:
        names_list.append(name.replace("\n",""))

# write emails
for name in names_list:
    with open(f'./Output/ReadyToSend/invitation_for_{name}.txt', mode='w') as file:
        file.write(email_content.replace("[name]",name))
