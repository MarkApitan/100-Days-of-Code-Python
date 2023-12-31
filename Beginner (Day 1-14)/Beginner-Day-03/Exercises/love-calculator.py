border = ("\033[0;35m---------------------------------------------------\033[0m")

print(border)
print("\033[0;31m\tWelcome to the Love Calculator!\033[0m")
print(border)

print("The Love Calculator is calculating your score...")
name1 = input("What is your Name? ") # What is your name?
name2 = input("What is your Partner's Name? ") # What is their name?
print (border)
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combined_name = name1+name2
lowername =combined_name.lower()

#For the first word
T = lowername.count("t")
R = lowername.count("r")
U = lowername.count("u")
E = lowername.count("e")

first_word = T+R+U+E


#for second word
L = lowername.count("l")
O = lowername.count("o")
V = lowername.count("v")
E = lowername.count("e")

second_word = L+O+V+E
love_score = int(str(first_word)+str(second_word))


if love_score <20:
  print(f"Your score is {love_score}, Friends")
elif love_score>=20 and love_score <40:
  print(f"Your score is {love_score}, Lovers.")
elif love_score>=40 and love_score<60:
  print(f"Your score is {love_score}, Affectionate.")
elif love_score>=60 and love_score<80:
  print(f"Your score is {love_score}, Marriage.")
elif love_score>=60 and love_score<80:
  print(f"Your score is {love_score}, Enemies.")
elif love_score>=80:
  print(f"Your score is {love_score}, Soulmate.")

#Friends, Lovers, Affectionate,Marrriage, Enemies, Soulmate