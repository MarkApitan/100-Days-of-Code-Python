#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
hard_password = []
border = ("\033[0;36m--------------------------------------------------------------------\033[0m")

print (border)
print("\033[0;35mWelcome to the PyPassword Generator!\033[0m")
print(border)

nr_letters= int(input("How many letters would you like in your password? ")) 
nr_symbols = int(input(f"How many symbols would you like? "))
nr_numbers = int(input(f"How many numbers would you like? "))
print(border)

hard_password_range = nr_letters + nr_symbols + nr_numbers
password_letter = ""
password_symbols = ""
password_numbers = ""
password_hard = ""
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

for x in range(1, nr_letters + 1):

    random_letter = random.randint (0, len(letters) - 1)
    letter = letters[random_letter]
    hard_password.append(letter)
    password_letter = password_letter + letter

for x in range (1, nr_symbols + 1):

    random_symbols = random.randint (0, len(symbols) - 1)
    symbol = symbols[random_symbols]
    hard_password.append(symbol)
    password_symbols = password_symbols + symbol

for x in range (1, nr_numbers + 1):
    random_numbers = random.randint(0, len(numbers) - 1)
    number = numbers[random_numbers]
    hard_password.append(number)
    password_numbers =  password_numbers + number

print (f"\033[0;32mGameEasy Password:\033[0m {password_letter}{password_numbers}{password_symbols}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

for x in range (1, hard_password_range+1):
    random_hard = random.randint(0, len(hard_password)-1)
    character = hard_password[random_hard]
    password_hard = password_hard + character

print(f"\033[0;32mGameHard Password:\033[0m {password_hard}")

print (border)
print ("\033[0;33mThank you for using PyPassword Generator!\033[0m")
print (border)