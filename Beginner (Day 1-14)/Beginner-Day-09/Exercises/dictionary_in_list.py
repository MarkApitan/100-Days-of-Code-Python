# Instructions
# You are going to write a program that adds to a travel_log. 
# You can see a travel_log which is a List that contains 2 Dictionaries. 
# Your job is to create a function that can add new countries to this list.

# add_new_country("Brazil", 5, ["Sao Paulo", "Rio de Janeiro"])
# DO NOT modify the travel_log directly. The goal is to create a function that modifies it.

# Example Input
# Brazil
# 5
# ["Sao Paulo", "Rio de Janeiro"]

# Example Output
# I've been to Brazil 5 times.
# My favourite city was Sao Paulo.

country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]

# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 

# Define a function called add_new_country that takes three parameters: country (a string), visits (an integer), and list_of_cities (a list).
def add_new_country(country:str, visits:int, list_of_cities:list):
    # Create an empty dictionary called new_country.
    new_country = {}
   
   # Add the values in the new_country dictionaru
    new_country["country"] = country
    new_country["visits"] = visits
    new_country["cities"] = list_of_cities

    # Append the new_country dictionary to the travel_log list.
    travel_log.append(new_country)
  
# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")