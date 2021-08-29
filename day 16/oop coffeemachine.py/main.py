from menu import Menu ,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
is_Turn_On=True
money=MoneyMachine()
dispenser=CoffeeMaker()
dispenser_menu=Menu()
while is_Turn_On:
    user_choice=input(f"What would you like? ({dispenser_menu.get_items()}) ").lower()
    if user_choice=='off':
        is_Turn_On=False
    if user_choice=='report':
        dispenser.report()
        money.report()
    else:
        drink=dispenser_menu.find_drink(user_choice)
        if drink !=None:
            if dispenser.is_resource_sufficient(drink):
                
                if money.make_payment(drink.cost):
                    dispenser.make_coffee(drink)
        else:
            print("This is not available")
