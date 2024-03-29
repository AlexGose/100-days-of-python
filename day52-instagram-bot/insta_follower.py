from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import os
import time

CHROMEDRIVER_PATH = "/opt/chromedriver"
INSTAGRAM_USERNAME = os.getenv('INSTAGRAM_USERNAME')
INSTAGRAM_PASSWORD = os.getenv('INSTAGRAM_PASSWORD')
SIMILAR_INSTAGRAM_ACCOUNT = os.getenv('SIMILAR_INSTAGRAM_ACCOUNT')


class InstaFollower:
    def __init__(self):
        self.driver = Chrome(service=Service(CHROMEDRIVER_PATH))
        self.username = INSTAGRAM_USERNAME
        self.password = INSTAGRAM_PASSWORD

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(10)
        user_name = self.driver.find_element(By.NAME, "username")
        user_name.send_keys(self.username)
        password = self.driver.find_element(By.NAME, "password")
        password.send_keys(self.password)
        login_button = self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        login_button.click()
        time.sleep(10)

    def find_followers(self):
        self.driver.get("https://www.instagram.com/" + SIMILAR_INSTAGRAM_ACCOUNT + "/followers/")
        time.sleep(15)
        xpath_string = "/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]" \
                       + "/div/div/div/div/div[2]/div/div/div[2]"
        modal = self.driver.find_element(By.XPATH, xpath_string)
        for _ in range(10):
            self.driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", modal)
            time.sleep(3)
        time.sleep(10)

    def follow(self):
        counter = 1
        while True:
            try:
                xpath_follow_button = "/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div" \
                                      + f"/div/div/div[2]/div/div/div[2]/div[1]/div/div[{counter}]/div/div" \
                                      + "/div/div[3]/div/button"
                follow_button = self.driver.find_element(By.XPATH, xpath_follow_button)
                follow_button.click()
            except ElementClickInterceptedException:
                time.sleep(2)
                xpath_cancel_button = "/html/body/div[2]/div/div/div[3]/div/div[2]/div[1]/div/div[2]" \
                               + "/div/div/div/div/div/div/button[2]"
                cancel_link = self.driver.find_element(By.XPATH, xpath_cancel_button)
                cancel_link.click()
            except NoSuchElementException:
                break
            else:
                counter += 1

            time.sleep(1)


if __name__ == '__main__':
    follower_bot = InstaFollower()
    follower_bot.login()
    follower_bot.find_followers()
    follower_bot.follow()
