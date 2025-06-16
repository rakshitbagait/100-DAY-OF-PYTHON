from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import ElementClickInterceptedException
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
SIMILAR_ACCOUNT="buzzfeedtasty"

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://www.instagram.com")
    def login(self):
        time.sleep(5)
        email_input =  self.driver.find_element(By.NAME,value="username")
        email_input.click()
        email_input.send_keys("xyz@gmail.com")
        time.sleep(2)
        password_input = self.driver.find_element(by=By.NAME,value="password")
        password_input.click()
        password_input.send_keys("xyz@",Keys.RETURN)
        time.sleep(2)
    def find_followers(self):
        time.sleep(10)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")
        time.sleep(8.2)
        # The xpath of the modal will change over time. Update yours accordingly.
        

        followers_link = self.driver.find_element(By.XPATH, '//a[contains(@href, "/followers/")]')
        followers_link.click()
        for i in range(5):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as an HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_link)
            time.sleep(2)

    def follow(self):
        # Check and update the (CSS) Selector for the "Follow" buttons as required.
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='._acan._acap._acas._aj1-._ap30')

        for button in all_buttons:
            try:
                button.click()
                time.sleep(1.1)
            # Clicking button for someone who is already being followed will trigger dialog to Unfollow/Cancel
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()