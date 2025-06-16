import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
web_page = response.text
soup = BeautifulSoup(web_page,"html.parser")
# print(soup.prettify())

addresses= soup.find_all("address")
# print(addresses)

address_list=[]

for address in addresses:
    text = address.get_text()
    address_list.append(text.strip())

# print(address_list)

prices = soup.find_all(name="span",class_="PropertyCardWrapper__StyledPriceLine")
price_list = [price.text.replace("+","").replace("/","").replace("mo","").replace("1 bd","").strip() for price in prices]
# print(price_list)

links = soup.find_all(name="a",class_="StyledPropertyCardDataArea-anchor")
links_list = [link.get('href') for link in links]
# print(links_list)

form_link = "https://forms.gle/cjtzmGVKTAavbDV97"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(url=form_link)

for submissions in range(len(address_list)+1):

    time.sleep(2)
    first_input = driver.find_element(by=By.XPATH,value='(//input[@class="whsOnd zHQkBf"])[1]')
    first_input.send_keys(address_list[submissions])
    time.sleep(2)
    second_input = driver.find_element(by=By.XPATH,value='(//input[@class="whsOnd zHQkBf"])[2]')
    second_input.send_keys(price_list[submissions])
    time.sleep(2)
    third_input = driver.find_element(by=By.XPATH,value='(//input[@class="whsOnd zHQkBf"])[3]')
    third_input.send_keys(links_list[submissions])
    time.sleep(2)
    submit_btn = driver.find_element(by=By.CSS_SELECTOR,value=".NPEfkd.RveJvd.snByac")
    submit_btn.click()
    time.sleep(5)
    driver.get(url=form_link)

    # driver.quit()