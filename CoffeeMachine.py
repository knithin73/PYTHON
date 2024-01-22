import os 
os.system('clear')

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
profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if resources[item] <= order_ingredients[item]:
            print(f"Sorry we don't have enought {item}")
            return False
        return True


def money():
    print("Please insert a coin: ")
    quarters=int(input("How many quarters : "))
    dime=int(input("How many dimes : "))
    nickles=int(input("How many nickles : "))
    pennies=int(input("How many pennies : "))
    total=(quarters*.25) + (dime*.1) + (nickles*.05) + (pennies*.01)
    return total

def is_trans_sufficient(payment, cost_drink):
    if payment >= cost_drink:
        change=round(payment-cost_drink, 2)
        global profit
        profit+=cost_drink
        print(f"Here is {change} dollas in change")
        return True
    else:
        print("Sorry that's not enough money")
        return False
    
def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Here's your {drink_name} ☕️ ")

is_on=True
while is_on:
    choice=input("what would you like to have espresso/latte/cappuccino : ")
    if choice=="off":
        is_on==False
    elif choice=='report':
        print(f"water:{resources['water']}")
        print(f"milk: {resources['milk']}")
        print(f"coffee: {resources['coffee']}")
        print(f"money: {profit} dollars")

    else:
        drink=MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment=money()
            is_trans_sufficient(payment,drink["cost"])
            make_coffee(choice,drink['ingredients'])


