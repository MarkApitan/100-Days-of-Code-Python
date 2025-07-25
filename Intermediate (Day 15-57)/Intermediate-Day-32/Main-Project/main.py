##################### Extra Hard Starting Project ######################
import smtplib  
import random   
import datetime as dt  
import pandas as pd
my_email = "toranagakwanu@gmail.com"
password = "itet idsm zfoo iiko"  
# 1. Update the birthdays.csv
letters = []
csv_file_path = r"c:\Users\User\OneDrive - Polytechnic University of the Philippines\Documents\100-Days-of-Code-Phyton\Intermediate (Day 15-57)\Intermediate-Day-32\Main-Project\birthdays.csv"
letter_1_file_path = r"c:\Users\User\OneDrive - Polytechnic University of the Philippines\Documents\100-Days-of-Code-Phyton\Intermediate (Day 15-57)\Intermediate-Day-32\Main-Project\letter_templates\letter_1.txt"
letter_2_file_path = r"c:\Users\User\OneDrive - Polytechnic University of the Philippines\Documents\100-Days-of-Code-Phyton\Intermediate (Day 15-57)\Intermediate-Day-32\Main-Project\letter_templates\letter_2.txt"
letter_3_file_path = r"c:\Users\User\OneDrive - Polytechnic University of the Philippines\Documents\100-Days-of-Code-Phyton\Intermediate (Day 15-57)\Intermediate-Day-32\Main-Project\letter_templates\letter_3.txt"

with open(letter_1_file_path) as file1, open(letter_2_file_path) as file2, open(letter_3_file_path) as file3:
    letter_1 = file1.read()
    letter_2 = file2.read()
    letter_3 = file3.read()
    letters += letter_1,letter_2,letter_3

# 2. Check if today matches a birthday in the birthdays.csv
day_today = dt.datetime.now()
df = pd.read_csv(csv_file_path)
birthdays_today = df[(df["month"] == day_today.month) & (df["day"] == day_today.day)]

if not birthdays_today.empty:
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    for index, rows in birthdays_today.iterrows():
        chosen_letter = random.choice(letters)
        personalized_letter = chosen_letter.replace("[NAME]", rows['name'])
    # 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()  # Secure the connection
            connection.login(user=my_email, password=password)  
            connection.sendmail(
                from_addr=my_email, 
                to_addrs=rows['email'], 
                msg=f"Subject:Happy Birthday!\n\n{personalized_letter}"
            )