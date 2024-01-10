
while True:

    num1 = float(input ("Enter first number: "))
    num2 = float(input ("Enter second number: "))
    num3 = float(input ("Enter third number: "))

    highest=0


    if num1 > num2 and num1 > num3:
        highest = num1
    elif num2 > num1 and num2 > num3:
        highest = num2
    elif num3 > num1 and num3> num2:
        highest = num3
    else: 
        print("All Numbers are equal")
        highest = num1

    print (f"The highest number is {highest}")

    use_again = input("Do you want to use the program again? (yes/no): ")
    if use_again == "no":
        print("Thank you for using the program")
    else: 
        print ("Welcome back to highest number adder program!")