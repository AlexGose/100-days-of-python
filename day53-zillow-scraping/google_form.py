from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os

CHROMEDRIVER_PATH = '/opt/chromedriver'
GOOGLE_FORM_URL = os.getenv('GOOGLE_FORM_URL')


class GoogleForm:
    def __init__(self, addresses, prices, links):
        self.driver = Chrome(service=Service(CHROMEDRIVER_PATH))
        self.addresses = addresses
        self.prices = prices
        self.links = links

    def submit_data(self):
        self.driver.get(GOOGLE_FORM_URL)
        time.sleep(10)
        for i in range(len(self.addresses)):
            xpath_address_input = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]' \
                                  + '/div/div/div[2]/div/div[1]/div/div[1]/input'
            xpath_price_input = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]' \
                                + '/div/div/div[2]/div/div[1]/div/div[1]/input'
            xpath_link_input = '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]' \
                               + '/div/div/div[2]/div/div[1]/div/div[1]/input'

            address_input = self.driver.find_element(By.XPATH, xpath_address_input)
            address_input.send_keys(self.addresses[i])

            price_input = self.driver.find_element(By.XPATH, xpath_price_input)
            price_input.send_keys(self.prices[i])

            link_input = self.driver.find_element(By.XPATH, xpath_link_input)
            link_input.send_keys(self.links[i])

            xpath_submit_button = '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span'
            submit_button = self.driver.find_element(By.XPATH, xpath_submit_button)
            submit_button.click()

            time.sleep(4)

            submit_another = self.driver.find_element(By.LINK_TEXT, "Submit another response")
            submit_another.click()

            time.sleep(4)


if __name__ == '__main__':
    gf = GoogleForm(['123 abc ave.', '333 fsdf'], ['$2999', '$2800'],
                    ['https://example.com/1', 'https://example.com/2'])
    gf.submit_data()
