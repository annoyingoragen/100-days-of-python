from data import resources, MENU
money=0

is_Turn_On=True

def check_resources(item):
    if item =='latte':
        if resources['coffee']<MENU['latte']['ingredients']['coffee']:
            print("sorry there is not enough coffee")
            return False
        elif resources['water']<MENU['latte']['ingredients']['water']:
            print("sorry there is not enough water")
            return False
        elif resources['milk']<MENU['latte']['ingredients']['milk']:
            print("sorry there is not enough milk")
            return False
        else:
            return True
    if item=='espresso':
        if resources['coffee']<MENU['espresso']['ingredients']['coffee']:
            print("sorry there is not enough coffee")
            return False
        elif resources['water']<MENU['espresso']['ingredients']['water']:
            print("sorry there is not enough water")
            return False
        else:
            return True
    if item=='cappuccino':
        if resources['coffee']<MENU['cappuccino']['ingredients']['coffee']:
            print("sorry there is not enough coffee")
            return False
        elif resources['water']<MENU['cappuccino']['ingredients']['water']:
            print("sorry there is not enough water")
            return False
        elif resources['milk']<MENU['cappuccino']['ingredients']['milk']:
            print("sorry there is not enough milk")
            return False
        else:
            return True


def money_input(item):
    quarters=int(input("How many quarters?"))
    dimes=int(input("How many dimes?"))
    nickles=int(input("How many nickles?"))
    pennies=int(input("How many pennies?"))
    total_input=0.25*quarters+0.1*dimes+0.05*nickles+0.01*pennies
    global money
    if item=="latte":
        if total_input<2.5:
            print("Sorry that's not enough money. Money refunded.")
            return False
        elif total_input>2.5:
            print(f"Here is ${round(total_input-2.5,2)} in change.")
            money+=2.5
            return True
        else:
            money+=total_input
            return True
    if item=="espresso":
        if total_input<1.5:
            print("Sorry that's not enough money. Money refunded.")
            return False
        elif total_input>1.5:
            print(f"Here is ${round(total_input-1.5,2)} in change.")
            money+=1.5
            return True
        else:
            money+=total_input
            return True
    if item=="cappuccino":
        if total_input<3.0:
            print("Sorry that's not enough money. Money refunded.")
            return False
        elif total_input>3.0:
            print(f"Here is ${round(total_input-3.0,2)} in change.")
            money+=3.0
            return True
        else:
            money+=total_input
            return True


def using_resources(item):
    if item =='latte':
        resources['coffee']-=MENU['latte']['ingredients']['coffee']
        resources['water']-=MENU['latte']['ingredients']['water']
        resources['milk']-=MENU['latte']['ingredients']['milk']
    if item=='espresso':
        resources['coffee']-=MENU['espresso']['ingredients']['coffee']
        resources['water']-=MENU['espresso']['ingredients']['water']
    if item=='cappuccino':
        resources['coffee']-=MENU['cappuccino']['ingredients']['coffee']
        resources['water']-=MENU['cappuccino']['ingredients']['water']
        resources['milk']-=MENU['cappuccino']['ingredients']['milk']


def greeting(item):
    if item=='latte':
        print("Here is your latte. enjoy!")
    if item=='cappuccino':
        print("Here is your cappuccino. enjoy!")
    if item=='espresso':
        print("Here is your espresso. enjoy!")


while is_Turn_On:
    user_choice=input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice=='report':
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\n"
        f"Coffee: {resources['coffee']}ml\nMoney: ${money}")
    if user_choice=='off':
        is_Turn_On=False
    is_enough_resources=check_resources(user_choice)
    if is_enough_resources:
        print("Please insert coins")
        is_enough_money=money_input(user_choice)
        if is_enough_money:
            using_resources(user_choice)
            greeting(user_choice)
   
  