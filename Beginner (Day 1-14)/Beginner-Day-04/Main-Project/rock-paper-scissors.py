rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

random_integer = random.randint(0,2)
set = [rock, paper, scissors]

#To print the score
def score(player_score, computer_score):
    print ("\033[1;33mScore:\033[0m")
    print (f"\033[0;32mPlayer:\033[0m {player_score}")
    print (f"\033[0;31mComputer:\033[0m {computer_score}")

#To display what the player and computer chose
def answer(int_player, computer):
    print ("\033[0;32mYou chose:")
    print (set[int_player])
    print ("\033[0;31mThe computer chose:")
    print (set[computer])

border = ("\033[0;36m---------------------------------------------------\033[0m")

#welcome introduction of the program
print (border)
print("\t\033[0;35mWelcome to Rock Paper Scissors Game\033[0m")
print (border)
print ("\033[0;31mInstructions:\033[0m")
print ("Type 0 for Rock \nType 1 for Paper \nType 2 for Scissors \nYou need 3 points to win. Goodluck!")
print (border)

player_score = 0
computer_score = 0
while True:
    computer = random.randint(0,2)
    player = input("What do you choose? ")
    int_player = int(float(player))
    print (border)
    #To check wheter who scores
    if int_player == computer:
        answer(int_player, computer)
        print (border)
        score(player_score, computer_score)
        print (border)
        
    elif int_player == 0 and computer == 2:
        answer(int_player, computer)
        print (border)
        player_score += 1
        score(player_score, computer_score)
        print (border)
        
    elif int_player == 2 and computer == 0:
        answer(int_player, computer)
        print (border)
        computer_score += 1
        score(player_score, computer_score)
        print(border)
        
    elif int_player == 2 and computer == 1:
        answer(int_player, computer)
        print (border)
        player_score += 1
        score(player_score, computer_score)
        print(border)
        
    elif int_player == 1 and computer == 2:
        answer(int_player, computer)
        print (border)
        computer_score += 1
        score(player_score, computer_score)
        print (border)
        
    elif int_player == 1 and computer == 0:
        answer(int_player, computer)
        print (border)
        player_score += 1
        score(player_score, computer_score)
        print(border)
        
    elif int_player == 0 and computer == 1:
        answer(int_player, computer)
        print (border)
        computer_score += 1
        score(player_score, computer_score)
        print (border)

    #To check if the input is invalid
    else:
        print ("Invalid Input")
        print(border)
    
    #To check whether who wins
    if player_score == 3:
        print ("\033[0;32mGame Over! You Win\033[0m")
        print (border)
        break
    elif computer_score == 3:
        print ("\033[0;31mGame Over! You Lose\033[0m")
        print (border)
        break