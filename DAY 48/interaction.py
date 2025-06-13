from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver= webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

# articles_link = driver.find_el9ement(By.CSS_SELECTOR, "#articlecount ul li:nth-child(2) a")
# print(articles_link.text)
# articles_link.click()
search = driver.find_element(By.CSS_SELECTOR, value =".vector-icon.mw-ui-icon-search.mw-ui-icon-wikimedia-search")
search.click()
serach_bar = driver.find_element(By.CLASS_NAME,value="cdx-text-input__input")
serach_bar.send_keys("Python",Keys.RETURN)



# driver.quit()