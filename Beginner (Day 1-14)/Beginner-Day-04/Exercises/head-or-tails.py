# Write your code below this line 👇
# Hint: Remember to import the random module first. 🎲
import random
border = ("\033[0;36m---------------------------------------------------\033[0m")
random_integer = random.randint(0, 1)

#welcome introduction of the program
print (border)
print("\t\t\b\b\b\bWelcome to Head or Tails Game")
print (border)

#to get the input
guess = input("Heads or Tails? ")
print (border)

#to make the input into a integer
if guess.lower() == "heads" or "head":
  int_guess = 1
elif guess.lower() == "tails" or "tail":
  int_guess = 0

#to generate the result
if random_integer == 1:
  print ("Guess: "+ guess)
  print ("Result: Heads")
  print (border)
else:
  print ("Guess: "+ guess)
  print ("Result: Tails")
  print (border)
