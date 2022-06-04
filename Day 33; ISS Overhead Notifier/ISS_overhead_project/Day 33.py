import requests
from datetime import datetime
import smtplib

MY_LAT = {"MY_LAT"} 
MY_LONG = {"MY_LONG"} 

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

position_close_to_iss = False
# Your position is within +5 or -5 degrees of the ISS position.
if MY_LAT-5 <+ iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
    position_close_to_iss = True

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) + 2
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) + 2

time_now = datetime.now()
current_hour = time_now.hour

# If the ISS is close to my current position
# and it is currently dark
if position_close_to_iss and sunrise > current_hour > sunset:
# Then send me an email to tell me to look up.
    my_email = f"{"MY_EMAIL"}"
    password = f"{"MY_PASSWORD"}"
    with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs={"RECEIVER_EMAIL"},
                            msg=f"Subject:Look up!\n\nThe ISS is flying over right now."
                            )

# BONUS: run the code every 60 seconds.



