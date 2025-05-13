import smtplib
import datetime as dt
import random
my_email ="rbagait2018@gmail.com"
password ="ypan zgfy iwhx hfuy"
now = dt.datetime.now()
weekday = now.weekday()
if weekday == 4:
    with open("D:/100 Days Of Python/DAY 32/quotes.txt") as quote_file:
        all_quotes =quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)

    with smtplib.SMTP("smtp.gmail.com",587) as connection :
       connection.starttls()
       connection.login(my_email,password=password)
       connection.sendmail(from_addr=my_email,
                           msg=f"Subject:Daily quotes\n\n{quote}",
                           to_addrs="rakshitbagaitpcm@gmail.com")
