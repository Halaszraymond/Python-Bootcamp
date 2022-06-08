from twilio.rest import Client
import smtplib
from day_40 import Day_40


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        self.TWILIO_SID = "AC09a26062f8573863cc0fb7ec5800f409"
        self.TWILIO_AUTH_TOKEN = "4561ac6edf3f26a2ca4acfd696ac844f"
        self.TWILIO_VIRTUAL_NUMBER = "+19784806248"
        self.TWILIO_VERIFIED_NUMBER = "+31613344119"
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
        my_email = "geenideejantje@yahoo.com"
        password = "okxjeqagdthrkfpt"
        with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            for receiver_email in emails:
                connection.sendmail(from_addr=my_email,
                                    to_addrs=receiver_email,
                                    msg=message
                                    )


