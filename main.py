from random import choice

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
money_machine = MoneyMachine()
menu = Menu()
coffee_maker = CoffeeMaker()
while True:
    options = menu.get_items()
    user_option = input(f"What will you like to take {options}")
    if user_option == "off":
        break
    elif user_option == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(user_option)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)



