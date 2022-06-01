##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import random
import smtplib
from csv import writer


# 1. Update the birthdays.csv
def update_csv(name, email, year, month, day):
    with open("birthdays.csv", "a") as data:
        new_row = [name, email, year, month, day]
        csv_writer = writer(data)
        csv_writer.writerow(new_row)


# 2. Check if today matches a birthday in the birthdays.csv
def birthday_check():
    df = pandas.read_csv("birthdays.csv")
    birthdays = df.to_dict(orient="records")
    now = dt.datetime.now()
    current_month = float(now.month)
    current_day = float(now.day)
    for birthday in birthdays:
        if birthday["month"] == current_month and birthday["day"] == current_day:
            name = birthday["name"]
            email = birthday["email"]
            contents_tuple = True, name, email
            return contents_tuple
        return False


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv
def random_letter(name):
    random_number = str(random.randint(1, 3))
    with open(f"letter_templates/letter_{random_number}.txt") as birthday_letter:
        contents = birthday_letter.read()
        contents = contents.replace("[NAME]", name)
        return contents


# 4. Send the letter generated in step 3 to that person's email address.
def send_email(receiver_email, letter):
    my_email = f"{You wish you knew this}"
    password = f"{strong password}"
    with smtplib.SMTP("smtp.?.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=receiver_email,
                            msg=f"Subject:Happy Birthday!\n\n{letter}."
                            )


add_name = input("Do you want to add a name: y or n")
if add_name == "y":
    the_name = input("What is the name of the person: ")
    the_email = input("What is the email of the person: ")
    the_year = input("In what year was the person born: ")
    the_month = int(input("In which month was the person born: (insert a number)"))
    the_day = int(input("On what day was the person born: (insert a number)"))
    update_csv(the_name, the_email, the_year, the_month, the_day)


if birthday_check():
    send_email(birthday_check()[2], random_letter(birthday_check()[1]))


