import smtplib
import random
import datetime as dt


def get_quote():
    with open("quotes.txt", "r") as quotes:
        list_of_quotes = [a_quote for a_quote in quotes]
        random_quote = random.choice(list_of_quotes)
        return random_quote


def send_email(the_quote):
    my_email = "geenideejantje@yahoo.com"
    password = "uohkxzwsimirnscc"
    with smtplib.SMTP("smtp.mail.yahoo.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email , password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="halaszraymond@gmail.com",
                            msg=f"Subject:Quote of the week\n\n{the_quote}."
                            )


def day_of_the_week():
    now = dt.datetime.now()
    day_of_week = now.weekday()
    return day_of_week


quote = get_quote()
weekday = day_of_the_week()

if weekday == 0:
    send_email(quote)
