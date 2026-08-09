from selenium import webdriver
import time
from selenium.webdriver.common.by import By
"""here import the libraries to automation
"""

# create chrome webDriver to open chrome
driver = webdriver.Chrome()

# Open google
driver.get("https://www.google.com")

# Maximize browser
driver.maximize_window()

# Keep browser open for 2 seconds
time.sleep(2)

driver.get("https://www.amazon.in")
time.sleep(2)

# First search the "Machine" appliance on search place
search_box = driver.find_element(By.XPATH, "//*[@id='twotabsearchtextbox']")
search_box.send_keys("machine")
button = driver.find_element(By.XPATH, "//*[@id='nav-search-submit-button']")
button.click()

# Go back to amazone home page
driver.back()
time.sleep(2)

# Refresh the website to re-use for "Iphone" Device.
driver.refresh()
time.sleep(2)

# here the search "Iphone" from users
search_box = driver.find_element(By.XPATH, "//*[@id='twotabsearchtextbox']")
search_box.send_keys("Iphones")
button = driver.find_element(By.XPATH, "//*[@id='nav-search-submit-button']")
button.click()

# Get the list of product in this class
proudct = driver.find_elements(By.XPATH, "//span[@class='a-size-medium a-color-base']")

for i in proudct:
    print(i.text)

input("Press any key to exit...")
driver.quit()
# Close browser
