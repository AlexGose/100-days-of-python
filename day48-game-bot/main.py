from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("/opt/chromedriver")
driver = webdriver.Chrome(service=service)

# driver.get('https://www.amazon.com/dp/B075CYMYK6')
# price = driver.find_element(By.CLASS_NAME, "a-offscreen")
# print(price.get_attribute('innerHTML'))

driver.get("https://www.python.org/")

# search_bar = driver.find_element(By.NAME, 'q')
# print(search_bar.get_attribute("place-holder"))
#
# logo = driver.find_element(By.CLASS_NAME, 'python-logo')
# print(logo.size)
#
# documentation_link = driver.find_element(By.CSS_SELECTOR, '.documentation-widget a')
# print(documentation_link.get_attribute("href"))
# print(documentation_link.text)
#
# print(driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[1]/div[3]/p[2]/a').text)

events_dict = {}
events_list = driver.find_elements(By.CSS_SELECTOR, '.event-widget li')
for index, event in enumerate(events_list):
    timestamp = event.find_element(By.TAG_NAME, 'time').get_attribute('datetime')
    events_dict[index] = {}
    events_dict[index]['time'] = timestamp[:10]
    events_dict[index]['name'] = event.find_element(By.TAG_NAME, 'a').text

print(events_dict)
driver.quit()
