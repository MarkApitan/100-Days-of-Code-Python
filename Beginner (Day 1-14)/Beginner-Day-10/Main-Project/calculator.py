def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operations  = {"+": add,
               "-": subtract,
               "x": multiply,
               "/": divide}

def calculator ():
    end_of_program = False

    n1 =  int(input("Enter First number: "))

    while end_of_program == False:

        print ("\nPick an operation to use, type:")
        print ("'+' to add \n'-' to subtract \n'x' to multiply \n'/' to divide")
        symbol = str(input("\nEnter the operator you want to use: "))

        n2 = int(input("\nEnter next number: "))

        result = operations[symbol](n1,n2)

        print (f"\n{n1} {symbol} {n2} = {result}")

        print ("\nEnter the following letter corresponding to your choice:\n'y' to continue calculating\n'n' to start a new calculation\n'e' to exit the program")    
        choice = input("\nEnter your choice: ").lower()
        if choice == 'y':
            n1 = result
        elif choice == 'n':
            calculator()
        else:
            print ("\nThank you for using the program!")
            end_of_program = True

calculator()