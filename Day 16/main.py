from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while 1 < 2:

    options = menu.get_items()
    coffee_choice = input(f"What would you like? {options}: ")
    coffee_choice = menu.find_drink(coffee_choice)

    if coffee_choice == "off":
        break
    elif coffee_choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(coffee_choice)
        if(coffee_maker.is_resource_sufficient(coffee_choice)):
            if(money_machine.make_payment(drink.cost)):
                coffee_maker.make_coffee(coffee_choice)
