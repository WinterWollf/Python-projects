# import csv
#
# with open("weather_data.csv", mode='r') as file:
#     date = csv.reader(file)
#
#     temperatures = []
#
#     for row in date:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
# print(temperatures)

import pandas

date = pandas.read_csv("weather_data.csv")
temperatures = date["temp"].to_list()

# avg_temperature = sum(temperatures) / len(temperatures)
# print(avg_temperature)

# avg_temperature = date["temp"].mean()
# print(avg_temperature)

max = date["temp"].max()
print(max)

print(date[date["temp"] == max])