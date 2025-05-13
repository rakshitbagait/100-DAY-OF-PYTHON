import datetime as dt
import pandas as pd
import os, random
import smtplib

# Email setup (use your credentials here)
MY_EMAIL = "rbagait2018@gmail.com"
MY_PASSWORD = "ypan zgfy iwhx hfuy"

today = dt.datetime.now()
today_tuple = (today.month, today.day)

# Load birthday data
birthday_file = pd.read_csv("D:/100 Days Of Python/DAY 32/birthdays.csv")

# Check for matching birthday
for index, row in birthday_file.iterrows():
    if (row['month'], row['day']) == today_tuple:
        # Pick a random letter template
        letter_templates_path = "D:/100 Days Of Python/DAY 32/letter_templates"
        letter_files = [f for f in os.listdir(letter_templates_path) if os.path.isfile(os.path.join(letter_templates_path, f))]
        random_letter = random.choice(letter_files)

        with open(os.path.join(letter_templates_path, random_letter)) as letter_file:
            content = letter_file.read()
            personalized_letter = content.replace("[NAME]", row['name'])

        # Send the email
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=row['email'],
                msg=f"Subject:Happy Birthday!\n\n{personalized_letter}"
            )
