from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
import os

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
        pass

    def find_followers(self):
        pass

    def follow(self):
        pass


if __name__ == '__main__':
    follower_bot = InstaFollower()
    follower_bot.login()
    follower_bot.find_followers()
    follower_bot.follow()
