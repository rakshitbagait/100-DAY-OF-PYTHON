from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")

# price_rupee = driver.find_element(By.CLASS_NAME,value="a-price-whole")

# print(f"The price is {price_rupee.text}")

search_bar = driver.find_element(By.ID,value="id-search-field")
print(search_bar.get_attribute("placeholder"))
button = driver.find_element(By.NAME,value="submit")
print(button.size)
documentation_link = driver.find_element(By.CSS_SELECTOR,value=".documentaion-widget a")
print(documentation_link.text)

driver.find_elements(By.NAME)
