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
data = pandas.read_csv("weather_data.csv")
print(data['temp'])