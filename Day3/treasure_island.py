
print("Welcome to the Treasure Island.\n Your mission is to find the treasure.")

action = input("You're at a cross-road. Where do you want to go? Type 'Left' or 'Right'. ")
if (action.lower() != 'left') :
    # means the user selected right or something else
    print("You fell in a hole. You died. GAME OVER!.")
    exit()

action = input("You come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across. ")

if action.lower() != 'wait':
    print("You got attacked by Trout. You died. GAME OVER!!.")
    exit()
action = input("You arrive at the island unharmed. There is a house with 3 doors. Red, Yellow and Blue. Which color do you choose? ")

if action.lower() == 'red':
    print("You got burned by fire. GAME OVER!")
    exit()

if action.lower() == 'blue':
    print("You got attacked and eaten up by a Beast. You are dead. GAME OVER!.")
    exit()

if action.lower() == 'yellow':
    print("You found the treasure. You WIN!")


