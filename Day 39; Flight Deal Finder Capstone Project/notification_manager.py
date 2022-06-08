from twilio.rest import Client
import smtplib
from day_40 import Day_40


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        self.TWILIO_SID = "{TWILIO_SID}"
        self.TWILIO_AUTH_TOKEN = "{TWILIO_AUTH_TOKEN}"
        self.TWILIO_VIRTUAL_NUMBER = "{TWILIO_PHONE_NUMBER"
        self.TWILIO_VERIFIED_NUMBER = "{YOUR_PHONE_NUMBER}"
        self.client = Client(self.TWILIO_SID, self.TWILIO_AUTH_TOKEN)

    def send_message(self, message):
        self.client.messages.create(
            body=message,
            from_=self.TWILIO_VIRTUAL_NUMBER,
            to=self.TWILIO_VERIFIED_NUMBER
        )
        return

    def send_email(self, message):
        emails = Day_40().list_of_emails()
        my_email = "{YOUR_EMAIL_ADDRESS}"
        password = "{YOUR_PASSWORD}"
        with smtplib.SMTP("smtp.?.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            for receiver_email in emails:
                connection.sendmail(from_addr=my_email,
                                    to_addrs=receiver_email,
                                    msg=message
                                    )


