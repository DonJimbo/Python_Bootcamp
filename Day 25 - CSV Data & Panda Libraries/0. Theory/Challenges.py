import csv
import pandas

from Theory.main import monday

data = pandas.read_csv("weather_data.csv")
temp_list = data["temp"].to_list()
print(len(temp_list))


'''
Challenge 5 - Convert Monday's temp to Fahrenheit
'''
monday = data[data.day == "Monday"]
monday_celsius = monday.temp[0]
monday_fahrenheit = (monday*(9/5))+32

'''
Challenge 4 - Row of data which had the highest temperature
'''

print(data[data.temp == data.temp.max()])

'''
Challenge 4 - Max value of temperature' series
'''

data["temp"].max()

'''
Challenge 3 - Find average temperature
'''

average = sum(temp_list) / len(temp_list)
print(average)

#or

data["temp"].mean()

'''
Challenge 2
'''

with open ("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperature = []
    for row in data:
        if row [1] != "temp":
            temperature.append(int(row[1]))
    print(temperature)


'''
Challenge 1
'''
with open ("weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)
