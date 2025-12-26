import pandas

data = pandas.read_csv("weather_data.csv")
print(type(data))
print(data["temp"])
print(type(data["temp"]))

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(len(temp_list))

# Get data in Columns
print(data["condition"])
print(data.condition)

# Get data in Rows
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

# Specific value in Row
monday = data[data.day == "Monday"]
print(monday.condition)

# Create a dataframe from scratch
data_dict_2 = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
data_2 = pandas.DataFrame(data_dict_2)
print(data_2)

# To create a new CSV file
data_2.to_csv("new_data.csv")