#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#Write your code below this line 👇
border = ("\033[0;36m----------------------------------------------------------------------------\033[0m")
#1. Welcome Message
print(border)
print("\033[0;35m\t\t\tWelcome to the Tip Calculator!\033[0m")
print(border)

#2. To get the inputs
total_bill =  float(input("What was the total bill? ₱"))
percentage =  int(input ("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input ("How many people to split the bill? "))
print(border)

#3. To calculate
new_percentage = percentage / 100
tip = total_bill * new_percentage
new_total_bill = (total_bill + tip) / people
round_total_bill = round(new_total_bill,2)
round_total_bill = "{:.2f}".format(new_total_bill)

#4. To print the results
print(f"\033[0;32mEach person should pay:\033[0m ₱{round_total_bill}")
print(border)
print("\033[0;33mThank you for using Tip Calculator\033[0m")
print(border)