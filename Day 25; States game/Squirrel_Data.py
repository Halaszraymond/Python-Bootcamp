import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_fur = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_fur = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_fur = len(data[data["Primary Fur Color"] == "Black"])

dictionary = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_fur, cinnamon_fur, black_fur]
}

df = pandas.DataFrame(dictionary)
df.to_csv("squirrel_count.csv")
