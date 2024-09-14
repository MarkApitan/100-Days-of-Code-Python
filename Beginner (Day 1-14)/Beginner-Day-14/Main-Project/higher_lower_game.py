# Import evrything that we need
import random
from art import logo
from art import border
from art import versus
from clear import Clear
from game_data import data

# Update choices for the next round, ensuring no duplicates.
def game_continue(first_choice, second_choice):
    first_choice = second_choice
    second_choice = random.choice(data)
    if first_choice == second_choice:
        second_choice = random.choice(data)
    Clear()
    return first_choice, second_choice

# Check if the user's answer is correct.t
def check_answer():
    if user_answer == 'a' and first_choice['follower_count'] > second_choice['follower_count']:
        return True
    elif user_answer == 'b' and first_choice['follower_count'] < second_choice['follower_count']:
        return True
    else:
        return False

# Pick 2 from the list
random_choices = random.sample(data, 2)
first_choice, second_choice = random_choices
score = 0
game_over = False
# Main game loop
while game_over == False:
    print(f"\033[1;33m{logo}\033[0m\n{border}")
    if score != 0:
        print(f"\033[0;32mYou're Right!\033[0m Current score:\033[0;32m {score}\033[0m")
    print(f"Compare A: {first_choice ['name']}, a {first_choice ['description']}, from {first_choice ['country']}." )
    print(f"\033[1;33m{versus}\033[0m")
    print(f"Against B: {second_choice ['name']}, a {second_choice  ['description']}, from {second_choice  ['country']}.\n{border}" )

    # Make the player pick
    user_answer = input("Who has more followers? (A/B): ").lower()

    # Check if the answer is right
    if check_answer() == True:
        score += 1
        first_choice, second_choice = game_continue(first_choice, second_choice)
    else:
        print(f"{border}\nSorry, that's \033[0;31mwrong\033[0m. Final score: \033[0;31m{score}\033[0m\n{border}")
        game_over = True