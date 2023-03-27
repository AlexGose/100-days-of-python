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

if __name__ == '__main__':
    done = False

    while not done:
        drink = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if drink == 'off': # hidden option for maintainers
            done = True
        elif drink == 'report':
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${money:0.2f}")
        else:
            print(f"{drink=}")  # temp test code

            # TODO: 4. print message if insufficient resources after beverage choice

            # TODO: 5. if sufficient resources after choice, prompt for coins

            # TODO: 6. process coins

            # TODO: 7. print message if insufficient money and give refund

            # TODO: 8. if sufficient money, give any change and add to revenue

            # TODO: 9. Make coffee, deduct ingredients from inventory

            # TODO: 10. Give beverage to customer