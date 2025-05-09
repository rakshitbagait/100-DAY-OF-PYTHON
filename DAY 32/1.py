# import smtplib

# my_email ="rbagait2018@gmail.com"
# password ="ypan zgfy iwhx hfuy"
# connection =smtplib.SMTP("smtp.gmail.com",587)
# connection.starttls()
# connection.login(user=my_email,password=password)
# connection.sendmail(from_addr=my_email,to_addrs="rakshitbagaitpcm@gmail.com",msg="Subject:hello\n\nThis is a new mail")
# connection.close()

 
import datetime as dt

now=dt.datetime.now()
year=now.year
date=now.date()
month = now.month
day = now.weekday()
print(day)
print(date)
print(month)
