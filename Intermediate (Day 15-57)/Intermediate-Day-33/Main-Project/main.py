import requests
from datetime import datetime
import smtplib  
import time

MY_LAT = 14.655828 #
MY_LONG = 120.966566 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
def is_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT+5 >= iss_latitude >= MY_LAT-5 and MY_LONG+5 >= iss_longitude >= MY_LONG-5:
        return True
    return False

def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    hour = time_now.hour
    if hour >= sunset or hour <= sunrise:
        return True
    return False

def send_email():
    my_email = "toranagakwanu@gmail.com"
    password = "itet idsm zfoo iiko"  
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()  # Secure the connection
        connection.login(user=my_email, password=password)  
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=my_email, 
            msg=f"Subject:Look UP!\n\nThe ISS is above you, look up!"
            )

#If the ISS is close to my current position
# and it is currently dark
while True:
    time.sleep(60)
    if is_close() and is_dark():
        send_email()
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.