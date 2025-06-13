import requests 
from bs4 import BeautifulSoup
import os 
from dotenv import load_dotenv
import smtplib
load_dotenv()

EMAIL = os.environ.get("EMAIL")
PASSWORD= os.environ.get("PASSWORD")

URL = "https://www.amazon.in/LG-Inverter-Frost-Free-Refrigerator-GL-I292RPZX/dp/B08X72GY5Q/ref=sr_1_9?_encoding=UTF8&rps=1&s=kitchen&sr=1-9"

headers = {
    "upgrade-insecure-requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    "sec-gpc": "1",
    "Accept-Language": "en-US,en;q=0.8",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "sec-ch-ua": "\"Brave\";v=\"137\", \"Chromium\";v=\"137\", \"Not/A)Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "priority": "u=0, i",
    "Cookie": "PHPSESSID=205b8c38b263e821bd9eb0a905ae2ceb",
    "x-forwarded-proto": "https",
    "x-https": "on",
    "X-Forwarded-For": "49.36.240.98"
}


response  = requests.get(url=URL,headers=headers)
web_page = response.text

soup=BeautifulSoup(web_page,"html.parser")
price = soup.find(name="span",class_="a-price-whole")

if price :
    price_text =price.get_text(strip=True)
    price_value =  float(price_text.replace(",", "")) 
    
    if price_value<25000:
        connection = smtplib.SMTP("smtp.gmail.com",587)
        connection.starttls()
        connection.login(user=EMAIL,password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,to_addrs="rakshitbagaitpcm@gmail.com",msg=f"Subject:Price dropping\n\n the price of fridge is below 25000\n{URL}")
        print("email sent!")

   
else:
    print("Price not found. Amazon may be blocking requests or the class has changed.")

