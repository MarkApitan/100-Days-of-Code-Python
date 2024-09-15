from data import MENU, resources

# TODO 2: Turn off the Coffee Machine by entering off to the promt
def off():
    print("Powering down... The coffee machine is going to sleep. ☕️💤")
    return True

# TODO 3: Print report
def report():
    print (f"Water: {resources['water']}")
    print (f"Milk: {resources['milk']}")
    print (f"Coffee: {resources['coffee']}")

# TODO 4: Check resources if sufficient
def check_resources(prompt):
    drink = promt
    water_needed = MENU[f"{drink}"]['ingredients']['water']
    milk_needed = MENU[f"{drink}"]['ingredients']['milk']
    coffee_needed = MENU[f"{drink}"]['ingredients']['coffee']

    water_left = resources['water']
    milk_left = resources['milk']
    coffee_left = resources['coffee']

    if drink == 'espresso':
        return water_needed <= water_left and coffee_needed <=coffee_left
    elif drink == 'latte' or 'cappuccino':
        return water_needed <= water_left and milk_needed <= milk_left and coffee_needed <=coffee_left

# TODO 1: Promt user by asking "What would you like?"

end_of_program = False
while not end_of_program:
    promt = input("What would you like? ").lower()
    if promt == 'off':
        end_of_program = off()
    elif promt == 'report':
        report()

