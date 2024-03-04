import pandas

all_date = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

color_list = all_date["Primary Fur Color"].to_list()

gray_count = color_list.count("Gray")
cinnamon_count = color_list.count("Cinnamon")
black_count = color_list.count("Black")

dict = {"Fur Color": ["Gray", "Cinnamon", "Black"],
        "Count": [gray_count, cinnamon_count, black_count]}

color_table = pandas.DataFrame(dict)

print(color_table)
