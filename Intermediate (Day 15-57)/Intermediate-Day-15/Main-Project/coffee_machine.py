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

# TODO 1: Promt user by asking "What would you like?"

end_of_program = False
while not end_of_program:
    promt = input("What would you like? ").lower()
    if promt == 'off':
        end_of_program = off()
    elif promt == 'report':
        report()

