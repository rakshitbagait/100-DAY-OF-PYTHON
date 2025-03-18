from menu import MENU,resources
profit =0
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item]>=resources[item]:
            print(f"sorry there is not enough {item}.")
            return False
        return True
def process_coins():
    print("please in(sert coins")
    total= int(input("how many quarters?"))*0.25
    total+= int(input("How many dimes"))*0.1
    total += int(input("how many nickles"))*0.5
    total += int(input("how many pennies"))*0.01
    return total
def is_transaction_successful(money_recieved, drink_cost):
    """Return True when the payment is accepte or False if the money is insufficient"""
    if money_recieved>=drink_cost:
        change = round(money_recieved-drink_cost,2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money.")
        return False
    
def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}☕")
while True:
    choice =input("What would you like? (espresso/latte/cappuccino):").lower()

    if choice =="off":
        break
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Water: {resources['milk']}ml")
        print(f"Water: {resources['coffee']}ml")
        print(f"Money:${profit}")
    else:
        drink =MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment =process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])
            print()

