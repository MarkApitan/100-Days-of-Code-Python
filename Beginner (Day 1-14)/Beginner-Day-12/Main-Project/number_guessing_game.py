import random
BORDER =("--------------------------------------------------------------------")
def choose_difficulty(choice):
    global BORDER
    if choice == 'easy':
        return 10
    elif choice == 'hard':
        return 5
    else:
        print (f"{BORDER}\n\033[0;31mInvalid\n\033[0m{BORDER}")
        exit()

# Check if the guess if correct. If not, checks if too high or too low
def guess_checker(guess, number):
    global BORDER 
    if guess.isnumeric():
        if int(guess) == number:
            print(f"\033[0;32mYou got it! the answer was {number}.\033[0m\n{BORDER}")
            return True
        elif int(guess) > number:
            print("\033[0;31mToo High.\033[0m")
            return False
        elif int(guess) < number:
            print("\033[0;31mToo Low.\033[0m")
            return False
    else:
        print("\033[0;31mInvalid input! Please enter a number.\033[0m")
        return False
    
# Generate a random number from 1 - 100
def main():
    global BORDER
    number = random.randint(1,100)
    print(f"{BORDER}\n\t\tWelcome to the number Guessing game!\n{BORDER}\nI'm thingking of a number between 1 and 100")
    # Make the player pick the difficulty

    choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    attempts = choose_difficulty(choice)
    print(BORDER)
    # Let the player guess and loop until the player run outs of attempts

    while attempts > 0:
        print (f"You have {attempts} attempts remaining to guess the number.")
        guess = input("Make a guess: ")
        if guess_checker(guess, number) == True:
            exit()
        else:
            attempts -= 1

        if attempts == 0:
            print ("\033[0;31mYou've run out of guesses, you lose.\033[0m")
            print(BORDER)
        else:
            print("Guess again")
            print(BORDER)
main()