# Coffee-machine
from menu import MENU, resources


def resource_subtracting(type_of_coffee):
    """Subtracts amount of Water, Milk and Coffee from Resources."""
    for ingredient, amount in MENU[type_of_coffee]['ingredients'].items():
        resources[ingredient] -= amount


def check_resources(type_of_coffee):
    """Checks if you have enough resources"""
    for ingredient, amount in MENU[type_of_coffee]['ingredients'].items():
        if resources[ingredient] < amount:
            print(f"Sorry, not enough {ingredient}.")
            return 0


def get_money():
    """Evaluates how much you are paying."""
    coin_amount = {
        "penny": 0.01,
        "dime": 0.10,
        "nickel": 0.05,
        "quarter": 0.25,
    }

    penny_sum = int(input("How many penny's?: ")) * coin_amount["penny"]
    dime_sum = int(input("How many dime's?: ")) * coin_amount["dime"]
    nickel_sum = int(input("How many nickel's?: ")) * coin_amount["nickel"]
    quarter_sum = int(input("How many quarter's?: ")) * coin_amount["quarter"]
    sum_money = penny_sum + dime_sum + nickel_sum + quarter_sum
    return float(sum_money)


def serve(type_of_coffee):
    """Serves the right product depending on your order."""
    amount_paid = 0
    print(f"{type_of_coffee.title()} cost's ${float(MENU[type_of_coffee]['cost'])}.")
    amount_paid = float(get_money())
    print(f"You paid ${amount_paid}")
    while not MENU[type_of_coffee]['cost'] == amount_paid:
        print(f"You paid only ${amount_paid}, please correct.")
        amount_paid = get_money()
    print(f"Here is your {type_of_coffee.title()}. Have a good day.")
    resources["money"] += float(amount_paid)


def report():
    """Gets a report"""
    print(resources)


def coffee_machine():
    """Starts the machine"""
    end_order = False

    while not end_order:
        inputs = ["espresso", "latte", "cappuccino", "report", "end"]
        order = input("What would you like?: ").lower()

        while order not in inputs:
            order = input("Invalid input. What would you like?: ").lower()

        if order == "report":
            report()
        elif order == "end":
            end_order = True
        else:
            if check_resources(order) == 0:
                end_order = True
        serve(order)
        resource_subtracting(order)


coffee_machine()
# coin input
