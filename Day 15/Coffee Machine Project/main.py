MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0

def check_resources(coffee):
    ingredients = MENU[coffee]["ingredients"]

    for ingredient, amount in ingredients.items():
        if resources[ingredient] < amount:
            return f"Sorry there is not enough {ingredient}."

    return True


def count_money(pennies, dimes, nickles, quarters, coffee):
    money_inserted = pennies * 0.01 + dimes * 0.10 + nickles * 0.05 + quarters * 0.25
    money_inserted = round(money_inserted, 2)  # Round the total

    if money_inserted >= MENU[coffee]['cost']:
        return money_inserted, True
    else:
        return money_inserted, False

def make_coffee(coffee, money_inserted):

    global money
    global resources

    money += MENU[coffee]['cost']
    print(f"Here is ${money_inserted - MENU[coffee]['cost']} dollars in change.")

    ingredients = MENU[coffee]["ingredients"]
    for ingredient, amount in ingredients.items():
        resources[ingredient] -= amount

    print(f"here is your {coffee}. Enjoy!")
    return


while 1 < 2:
    coffee_choice = input("What would you like? (espresso/latte/cappuccino):")

    if coffee_choice == "off":
        break
    elif coffee_choice == "report":
        print(f"Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${money}")
        continue

    sufficient_resources = check_resources(coffee_choice)
    if type(sufficient_resources) == str:
        break

    quarters = float(input("How many quarters? "))
    dimes = float(input("How many dimes? "))
    nickles = float(input("How many nickles? "))
    pennies = float(input("How many pennies? "))
    money_inserted, enough_money = count_money(pennies, dimes, nickles, quarters, coffee_choice)

    if enough_money is True:
        make_coffee(coffee_choice, money_inserted)
    else:
        print("Sorry that's not enough money. Money refunded.")
