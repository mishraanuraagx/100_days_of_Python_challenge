from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def main():
    menu = Menu()
    money_Machine = MoneyMachine()
    coffee_maker = CoffeeMaker()
    machine_running = True
    while machine_running:
        action = input("What would you like to order? " + menu.get_items())
        action = action.lower()
        if action == 'report':
            print(coffee_maker.report())
            print(money_Machine.report())
        elif action == 'off':
            machine_running = False
        else:
            # make coffee
            drink = menu.find_drink(action)
            resources_available = coffee_maker.is_resource_sufficient(drink)
            if drink and resources_available:
                money_received = money_Machine.make_payment(drink.cost)
                if money_received:
                    coffee_maker.make_coffee(drink)


main()