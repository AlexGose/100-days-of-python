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


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money:0.2f}")


def resource_is_sufficient(beverage, resource):
    if beverage == 'espresso' and resource == 'milk':  # no milk ingredient
        return True
    else:
        return resources[resource] >= MENU[beverage]['ingredients'][resource]


def resources_are_sufficient(beverage):
    for resource in resources:
        if not resource_is_sufficient(beverage, resource):
            return False
    return True


def get_coins():
    output = {'quarters': 0, 'dimes': 0, 'nickles': 0, 'pennies': 0}
    for coin in output:
        output[coin] = int(input(f"how many {coin}? "))
    return output


def get_value(coins_dict):
    value = 0
    for coin in coins_dict:
        if coin == 'quarters':
            value += 0.25 * coins_dict[coin]
        elif coin == 'dimes':
            value += 0.10 * coins_dict[coin]
        elif coin == 'nickles':
            value += 0.05 * coins_dict[coin]
        elif coin == 'pennies':
            value += 0.01 * coins_dict[coin]
    return value


if __name__ == '__main__':
    done = False

    while not done:
        drink = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if drink == 'off':  # hidden option for maintainers
            done = True
        elif drink == 'report':
            print_report()
        else:
            print(f"{drink=}")  # temp test code
            resources['water'] = 200  # temp test code

            for ingredient in resources:
                if not resource_is_sufficient(drink, ingredient):
                    print(f"Sorry there is not enough {ingredient}.")

            if resources_are_sufficient(drink):
                coins = get_coins()

                payment = get_value(coins)
                print(f"{payment=}")  # temp test code

                # TODO: 7. print message if insufficient money and give refund

                # TODO: 8. if sufficient money, give any change and add to revenue

                # TODO: 9. Make coffee, deduct ingredients from inventory

                # TODO: 10. Give beverage to customer