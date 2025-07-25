# This App sends Motivational quotes on monday via Email
import smtplib  
import random   
import datetime as dt  

my_email = "toranagakwanu@gmail.com"
password = "itet idsm zfoo iiko"  

# Get current date and extract the day of the week (0=Monday, 6=Sunday)
day_today = dt.datetime.now()
day_of_the_week = day_today.weekday()

# Read all quotes from the file into a list and pick one at random
with open(r"c:\Users\User\OneDrive - Polytechnic University of the Philippines\Documents\100-Days-of-Code-Phyton\Intermediate (Day 15-57)\Intermediate-Day-32\Challenges\quotes.txt","r") as file:
    quotes_list = file.readlines()
    random_quote = random.choice(quotes_list)

# If today is Friday (4), send the email with the random quote
if day_of_the_week == 0:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # Secure the connection
        connection.login(user=my_email, password=password)  
        connection.sendmail(
            from_addr=my_email, 
            to_addrs="markpogiszxc@gmail.com", 
            msg=f"Subject:Motivational Quote of the Day\n\n{random_quote}"
        )