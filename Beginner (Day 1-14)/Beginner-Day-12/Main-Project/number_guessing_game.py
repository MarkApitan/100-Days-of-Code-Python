import random

def choose_difficulty(choice):
    
    if choice == 'easy':
        return 10
    elif choice == 'hard':
        return 5
    else:
        print ("Invalid")
        exit()

# Check if the guess if correct. If not, checks if too high or too low
def guess_checker(guess, number):
    if guess.isnumeric():
        if int(guess) == number:
            print(f"You got it! the answer was {number}.")
            return True
        elif int(guess) > number:
            print("Too High.")
            return False
        elif int(guess) < number:
            print("Too Low.")
            return False
    else:
        print("Invalid input! Please enter a number.")
        return False
    
# Generate a random number from 1 - 100
def main():
    number = random.randint(1,100)
    print("Welcome to the number Guessing game!\nI'm thingking of a number between 1 and 100")
    # Make the player pick the difficulty

    choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    attempts = choose_difficulty(choice)
    # Let the player guess and loop until the player run outs of attempts

    while attempts > 0:
        print (f"You have {attempts} attempts remaining to guess the number.")
        guess = input("Make a guess: ")
        if guess_checker(guess, number) == True:
            exit()
        else:
            attempts -= 1

        if attempts == 0:
            print ("You've run out of guesses, you lose.")
        else:
            print("Guess again")
main()