import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
primary_color_list = data['Primary Fur Color'].to_list()
gray_count = data['Primary Fur Color'].value_counts()["Gray"]
red_count = data['Primary Fur Color'].value_counts()["Cinnamon"]
black_count = data['Primary Fur Color'].value_counts()["Black"]

color_count_dict = {"Fur Color": ["Gray", "Cinnamon", "Black"],
                    "Counts": [gray_count, red_count, black_count]}

color_count_df = pandas.DataFrame(color_count_dict)
color_count_df.to_csv('squirrel_count.csv')