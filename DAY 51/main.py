from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os 
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
Email = os.getenv("EMAIL")
Password = os.environ.get("PASSWORD")
PROMISED_DOWN = 150
PROMISED_UP = 10
URL = "https://twitter.com/login"
class InternetSpeedTwitterBot:
    def __init__(self):
        
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach",True)
        self.driver  = webdriver.Chrome(options=self.chrome_options)
        
        self.up =0
        self.down = 0
    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.continue_btn =self.driver.find_element(by=By.ID,value="onetrust-accept-btn-handler")
        self.continue_btn.click()
        self.go_btn = self.driver.find_element(by=By.CLASS_NAME,value="start-text")
        self.go_btn.click()
        time.sleep(60)
        self.down_speed = self.driver.find_element(by=By.CSS_SELECTOR,value=".result-data-large.number.result-data-value.download-speed")
        print(self.down_speed.text)
        self.up_speed = self.driver.find_element(by=By.CSS_SELECTOR,value=".result-data-large.number.result-data-value.upload-speed").text
        print(self.up_speed)
    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")

        time.sleep(2)
        email = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input')
        password = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input')

        email.send_keys("your mail")
        password.send_keys("You password")
        time.sleep(2)
        password.send_keys(Keys.ENTER)

        time.sleep(5)
        tweet_compose = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')

        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_compose.send_keys(tweet)
        time.sleep(3)

        tweet_button = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()

        time.sleep(2)
        self.driver.quit()

bot = InternetSpeedTwitterBot()
# bot.get_internet_speed()
bot.tweet_at_provider()