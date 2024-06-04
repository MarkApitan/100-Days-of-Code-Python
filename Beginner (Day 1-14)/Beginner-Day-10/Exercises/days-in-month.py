# Convert the is_leap() function
# In the starting code, you'll find the solution from the Leap Year challenge. 
# First, convert this function is_leap() so that instead of printing "Leap year." or "Not leap year." 
# it should return True if it is a leap year and return False if it is not a leap year.

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
# TODO: Add more code here 👇

# Create a new function called days_in_month()
# You are then going to modify a function called days_in_month() which will take a year and a month as inputs, e.g.
# days_in_month(year=2022, month=2)
# And it will use this information to work out if the year is a leap year and decide the number of days in the month, then return that as the output, e.g.:
# 28

def days_in_month(year:int, month:int):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
    if is_leap(year) == True and month == 2:
        return ("There are " + 29+ ' days')
    else:
        return f"There are {month_days[month-1]} days" 
    
#🚨 Do NOT change any of the code below 

year = int(input("Enter year: ")) # Enter a year
month = int(input("Enter month: ")) # Enter a month
days = days_in_month(year, month)
print(days)    