
row1 = [" ", " ", " ", " "]
row2 = [" ", " ", " ", " "]
row3 = [" ", " ", " ", " "]
row4 = [" ", " ", " ", " "]

treasure_map = [row1, row2, row3, row4]

position = input("Give a coordinate xy to place your treasure on 4x4 island.")

horizontal = int(position[0]) - 1
vertical = int(position[1]) - 1

treasure_map[vertical][horizontal] = "X"

print(f"{row1}\n{row2}\n{row3}\n{row4}")



