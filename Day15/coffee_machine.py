import os

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
money = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def welcome_screen():
    print("\n\nWelcome to the Coffee Machine.")
    action = input("What would you like? (espresso/latte/cappuccino): ")
    return action


def report():
    print(
        f" Water: {resources['water']}\n Milk: {resources['milk']}\n Coffee: {resources['coffee']}\n Profit: {profit}\n")


def check_resources(water: int, coffee: int, milk: int):
    if resources["water"] <= water:
        return False, "Sorry there is not enough water."
    elif resources["milk"] <= milk:
        return False, "Sorry there is not enough milk."
    elif resources["coffee"] <= coffee:
        return False, "Sorry there is not enough coffee."

    return True, "Requirement met."


def check_requirements(coffee: str):
    global profit
    message = ""
    status = True
    # check coffee req
    if MENU[coffee]:
        ingredients = MENU[coffee]['ingredients']
        resource_req_met, message = check_resources(ingredients['water'], ingredients['coffee'], ingredients['milk'])
        if not resource_req_met:
            print(message)
            status = False
            return status, message
        else:
            # take money
            money_processed, total_money_received = process_money(MENU[coffee]["cost"])
            if money_processed == False:
                return False, "Money processing issue."
            global money
            money = total_money_received
            # else:
            #     return_change = total_money_received - MENU[coffee]["cost"]
            #     profit += round(MENU[coffee]["cost"],2)
            #     print(f"Here is ${round(return_change,2)} in change.")
            #     make_coffee(coffee)


    else:
        message = "This coffee doesn't exist."
        print(message)
        status = False
        return status, message
    return status, message


def process_money(req_money: float):
    print("Please insert coins.")
    q_coins = int(input("How many quarters $0.25?: "))
    d_coins = int(input("How many dimes $0.1?: "))
    n_coins = int(input("How many nickels $0.05?: "))
    p_coins = int(input("How many pennies $0.01?: "))
    total_money_received = q_coins * 0.25 + d_coins * 0.1 * n_coins * 0.05 + p_coins * 0.01
    if total_money_received < req_money:
        print(
            f"Sorry, it is not enough to process this coffee. You entered ${round(total_money_received,2)} whereas we need ${req_money}")
        return False, total_money_received

    return True, total_money_received


def make_coffee(coffee: str):
    ingredients = MENU[coffee]["ingredients"]
    resources["water"] -= ingredients["water"]
    resources["coffee"] -= ingredients["coffee"]
    resources["milk"] -= ingredients["milk"]
    print(f"Here is your {coffee}. ☕")


def return_change(coffee: str):
    global money, profit
    return_change = money - MENU[coffee]["cost"]
    money = 0
    profit += round(MENU[coffee]["cost"], 2)
    print(f"Here is ${round(return_change, 2)} in change.")

def refill_coffee_machine():
    resources["water"] = 300
    resources["milk"] = 200
    resources["coffee"] = 100


def main():
    os.system('clc' if os.name == 'nt' else 'clear')
    machine_running = True
    while machine_running:
        action = welcome_screen()
        if action.lower() == 'report':
            report()
        elif action.lower() == 'refill':
            refill_coffee_machine()
        elif action.lower() == 'latte' or action.lower() == 'espresso' or action.lower() == 'cappuccino':
            proceed, message = check_requirements(action.lower())
            if proceed:
                make_coffee(action.lower())
                return_change(action.lower())

        elif action.lower() == 'off':
            machine_running = False
            print("Turning off the coffee machine now.")


main()
