from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service('/opt/chromedriver')
driver = webdriver.Chrome(service=service)

# driver.get("https://wikipedia.org")

# english_link = driver.find_element(By.CSS_SELECTOR, '#js-link-box-en small bdi')
# num_pages = english_link.text
# print(num_pages.replace(' ', ',').replace('+', ''))

# english_link.click()

# search_bar = driver.find_element(By.ID, 'searchInput')
# search_bar.send_keys("Python")
# search_bar.send_keys(Keys.ENTER)

driver.get("https://web.archive.org/web/20220120120408/https://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("asdf")
last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("asdfasdf")
email = driver.find_element(By.NAME, "email")
email.send_keys("asdf@asdfasdf.com")
sign_up = driver.find_element(By.CSS_SELECTOR, '.btn-primary')
sign_up.click()

driver.quit()
