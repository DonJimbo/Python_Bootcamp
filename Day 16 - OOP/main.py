from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_mach = MoneyMachine()
coffee_make = CoffeeMaker()
menu = Menu()
item = MenuItem ("","","","","",)

machine_on = True
while machine_on is True:
    choices = menu.get_items()
    order_name = input(f"Please select your drink, (available items, {choices}):")


    if order_name == "off":
        machine_on = False

    elif order_name == "report":
        coffee_make.report()
        money_mach.report()

    elif item:
        item = menu.find_drink(order_name)
        resources = coffee_make.is_resource_sufficient(item)
        if resources is True:
            profit = money_mach.make_payment(item.cost)
            if profit is True:
                coffee_make.make_coffee(item)
                coffee_make.report()
                money_mach.report()

