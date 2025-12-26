import pandas

# Connect CSV to variable
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Extract data for cvs
squirrels_grey_count= len(data[data["Primary_Fur_Color"] == "grey"])
squirrels_red_count = len(data[data["Primary_Fur_Color"] == "red"])
squirrels_black_count = len(data[data["Primary_Fur_Color"] == "black"])

# Create a table with the extracted data (with DataFrame)
data_dict_squirrels = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [squirrels_grey_count, squirrels_red_count, squirrels_black_count]
}
new_data = pandas.DataFrame(data_dict_squirrels)

# Make and print the table in a new CVS file
new_data.to_csv("squirrel_count.csv")