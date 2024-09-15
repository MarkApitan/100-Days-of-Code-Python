from data import MENU, resources, menu

# TODO 2: Turn off the Coffee Machine by entering off to the promt
def off():
    print("Powering down... The coffee machine is going to sleep. ☕️💤")
    return True

# TODO 3: Print report
def report():
    print (f"Water: {resources['water']}")
    print (f"Milk: {resources['milk']}")
    print (f"Coffee: {resources['coffee']}")
    print (f"Money: {profit}")

# TODO 4: Check resources if sufficient
def check_resources(prompt):
    drink = prompt
    water_needed = MENU[f"{drink}"]['ingredients']['water']
    coffee_needed = MENU[f"{drink}"]['ingredients']['coffee']
    water_left = resources['water']
    milk_left = resources['milk']
    coffee_left = resources['coffee']
    
    if not water_left >= water_needed:
        print("Sorry there is not enough water")
        return False
    elif not coffee_left >= coffee_needed:
        print("Sorry there is not enough coffee needed")
        return False
    elif drink in ['latte', 'cappuccino'] and not milk_left >= MENU[f"{drink}"]['ingredients']['milk']:
        print ("Sorry there is not enough milk left.")
        return False
    else:
        return True
    
# TODO 5: Process Coins
def process_coins():
    print("Please insert coins.")
    try:
        twenty = float(input("Enter the number of ₱20 coins: "))
        ten = float(input("Enter the number of ₱10 coins: "))
        five = float(input("Enter the number of ₱5 coins: "))
        one = float(input("Enter the number of ₱1 coins: "))
        centavos = float(input("Enter the number of ₱0.25 centavos: "))
        total_money = (20 * twenty) + (10 * ten) + (5 * five) + (1 * one) + (0.25 * centavos)
        return total_money, False
    except ValueError :
        print ("Error! Invalid Input, Refunding Money.")
        return 0, True

# TODO 6: Check Transaction
def check_transaction(money_inserted, prompt, profit):
    drink = prompt
    cost = MENU[f"{drink}"]['cost']

    if money_inserted >= cost:
        change = money_inserted - cost
        profit += cost
        print (f"Here is ₱{round(change, 2)} in change.")
        return profit, False
    else:
        print ("Sorry that's not enough money. Money refunded.")
        return 0, True

# TODO 7: Make Coffee
def make_coffee(prompt):
    for item in MENU[f"{prompt}"]['ingredients']:
        resources[item] -= MENU[f"{prompt}"]['ingredients'][f'{item}']
    print(f"\033[32mYour {prompt} is ready. Enjoy!☕️\033[0m") 

# TODO 1: Promt user by asking "What would you like?"
profit = 0
end_of_program = False
print(menu)
while end_of_program == False:
    prompt = input("What would you like? ").lower()
    if prompt == 'off':
        end_of_program = off()
    elif prompt == 'report':
        report()
    elif prompt in ['espresso', 'latte', 'cappuccino']:
        if check_resources(prompt):
            money_inserted, error_occurred = process_coins()
            if not error_occurred:
                profit, error_occurred = check_transaction(money_inserted, prompt, profit)
                if not error_occurred:
                    make_coffee(prompt)
                else:
                    end_of_program = off()
            else:
                end_of_program = off()
        else:
            end_of_program = off()
    else:
        print("Invalid")
        end_of_program = off()