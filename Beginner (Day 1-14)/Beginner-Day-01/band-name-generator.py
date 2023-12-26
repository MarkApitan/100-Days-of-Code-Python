border = ("---------------------------------------------------")
#1. Create a greeting for your program.
print (border)
print("\t\033[0;35mWelcome to the Band Name Generator\033[0m")
print (border)
#2. Ask the user for the city that they grew up in.
city = input("\033[0;32mWhat's name of the city you grew up in?\033[0m\n")

#3. Ask the user for the name of a pet.
pet = input("\033[0;32mWhat's your pet's name?\033[0m\n")

#4. Ask the user their favorite animal
animal = input("\033[0;32mWhat's your favorite animal?\033[0m\n")

#4. Combine the name of their city and pet and show them their band name.
print (border)
print ("\033[0;35mYour band name could be:\033[0m")
print ("\033[0;34mOption 1:\033[0m " + city + " " + pet )
print ("\033[0;34mOption 2:\033[0m " + animal + " " + pet )
print ("\033[0;34mOption 3:\033[0m " + city + " " + animal )

#5. Thank you greeting of the progra,
print(border)
print("\033[0;33mThank you for using Band Name Generator!\033[0m")
print(border)