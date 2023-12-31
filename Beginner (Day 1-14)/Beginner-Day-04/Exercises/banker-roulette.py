names_string = ["Otep", "Maihan", "Kwanu", "Blessie", "Susu", "Cholina"]
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
import random
numnames = len(names_string)
random = random.randint(0, numnames - 1)
pay = (names_string[random])
print (f"{pay} is going to buy the meal today!")