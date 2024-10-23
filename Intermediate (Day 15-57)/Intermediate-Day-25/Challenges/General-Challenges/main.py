# with open ("weather_data.csv", "r") as e:
#     read = e.readlines()
#
#     data = [line.strip() for line in read]
# print(data)

# import csv
# with open ("weather_data.csv", "r") as data_file:
#     data = csv.reader(data_file)
#     temperatures = [int(item[1]) for item in data if item[1] != "temp"]
# print(temperatures)

import pandas
# data = pandas.read_csv("weather_data.csv")
# print(data['temp'])

# Average temp challenge
# My solution
# list_temp = data['temp'].to_list()
# average = sum(list_temp) / len(list_temp)
# print(round(average,2))

# Simpler way using pandas
# print(data["temp"].mean())

# Getting the max value
# print(data['temp'].max())

# 2 ways to get data in columns
# print(data['temp'])
# print(data.temp)

# Getting the data in row
# print(data[data.day == 'Monday'])
# Getting the data in row where the temp is at highest
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == 'Monday']
# monday_temp = monday.temp[0]
# fahrenheight = (monday_temp * (9/5)) + 32
# print(fahrenheight)

# Create a dataframe from scratch
data_dict = {"students": ["sapata", "luigi", "lianza", "earl", "aidan"],
             "grades": [90, 91, 92, 93, 94]}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("data.csv")
