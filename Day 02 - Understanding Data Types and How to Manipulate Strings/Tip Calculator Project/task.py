from typing import final
from xml.dom.minidom import ProcessingInstruction

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_perc = 1+(tip/100)
final_amount = round((bill*tip_perc)/people,2)
print(f"Each person should pay: ${final_amount}")
