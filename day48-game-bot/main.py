from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

service = Service("/opt/chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, "cookie")

for k in range(60):  # loop finishes after 5 minutes
    for i in range(100):  # loop finishes after 5 seconds
        sleep(0.05)  # 5 milliseconds
        cookie.click()
    store = driver.find_element(By.ID, "store")
    items = store.find_elements(By.CSS_SELECTOR, 'div[onclick]')
    for item in items:
        if item.get_attribute("class") != "grayed":
            last_item = item
    last_item.click()  # get the most expensive item available

cps = driver.find_element(By.ID, "cps")
print(cps.text)

driver.quit()
