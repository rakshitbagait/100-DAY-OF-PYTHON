from selenium import webdriver
from selenium.webdriver.common.by import By
import time
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")
time.sleep(1)
cookie = driver.find_element(By.ID,value="cookie")
cookie.click()
cookie.click()


buyCursor = driver.find_element(By.ID,value="buyCursor")
def money_calc():
    cookie_money = driver.find_element(By.ID,"money")

    money = cookie_money.text
    return money
# driver.quit()

while True:
    cookie.click()
    print(money_calc())



