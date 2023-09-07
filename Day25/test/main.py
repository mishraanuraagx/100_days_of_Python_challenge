import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if row[1].isdigit():
            temperatures.append(int(row[1]))

    print(temperatures)

import pandas
data = pandas.read_csv("weather_data.csv")
print(data["temp"])

max_temp = data["temp"].max()
print(max_temp)

print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

data_dict = {
    "students": ["Amy","Anu","Ren"],
    "scores": ["70","99","100"]
}

dataframe = pandas.DataFrame(data_dict)
dataframe.to_csv("new_datadict.csv")
