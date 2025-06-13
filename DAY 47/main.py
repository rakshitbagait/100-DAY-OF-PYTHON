from bs4 import BeautifulSoup
import requests,os
from dotenv import load_dotenv
import smtplib
load_dotenv()
EMAIL= os.getenv("EMAIL")
PASSWORD= os.getenv("PASSWORD")
url = "https://appbrewery.github.io/instant_pot/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "Accept-Language": "en-IN,en;q=0.9"
}

response = requests.get(url=url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

price = soup.find("span", class_="a-price-whole")

if price:
    price_text = price.get_text(strip=True)   # e.g. '99'
    price_value = float(price_text.replace(",", "")) 
   
else:
    print("Price not found. Amazon may be blocking requests or the class has changed.")


message = ""
if price_value>90:
    connection = smtplib.SMTP("smtp.gmail.com",587)
    connection.starttls()
    connection.login(user=EMAIL,password=PASSWORD)
    connection.sendmail(from_addr=EMAIL,to_addrs="rakshitbagaitpcm@gmail.com",msg="Subject:price is higher\n\nThe price drops of the cooker")
    connection.close()
    print("email sent")