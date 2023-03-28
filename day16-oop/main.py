from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

cm = CoffeeMaker()
mm = MoneyMachine()
m = Menu()

done = False

while not done:
    drink = input(f"What would you like? ({m.get_items()}): ").lower()

    if drink == 'off':  # hidden option for maintainers
        done = True
    elif drink == 'report':
        cm.report()
        mm.report()
