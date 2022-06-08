import csv


class Day_40:

    def make_user(self):
        # inputs by user
        user_first_name = input("What is your first name: ").title()
        user_last_name = input("What is your last name: ").title()

        email_check = False

        while not email_check:
            user_email = input("What is your email: ")
            email_check = input("Write your email again: ")
            if user_email == email_check:
                print("You are in the club")
                email_check = True

        user_data = [user_first_name, user_last_name, user_email]
        writer = csv.writer(open("users.csv", "a"))
        writer.writerow(user_data)

    def list_of_emails(self):
        with open("users.csv", "r") as user_data:
            csvfile = csv.DictReader(user_data)
            emails = [line["Email"] for line in csvfile]
            return emails

