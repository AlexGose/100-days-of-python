from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

CHROMEDRIVER_PATH = '/opt/chromedriver'
ZILLOW_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination" \
             + "%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3" \
             + "A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.6926" \
             + "1345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C" \
             + "%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%2" \
             + "2value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%" \
             + "22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7" \
             + "B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A" \
             + "%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%" \
             + "7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%" \
             + "7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"


class ZillowScraper:
    def __init__(self):
        self.driver = Chrome(service=Service(CHROMEDRIVER_PATH))

    def open_webpage(self):
        self.driver.get(ZILLOW_URL)
        time.sleep(20)

    def scrape(self, address_list, price_list, link_list):
        listings = self.driver.find_elements(By.CLASS_NAME, 'StyledListCardWrapper-srp__sc-wtsrtn-0')
        for listing in listings:
            info = listing.text.split('\n')
            if len(info) == 1:  # skip advertisements
                continue
            address_list.append(info[0])
            price_list.append(info[1].split('+')[0].split('/')[0])
            link_list.append(listing.find_element(By.CLASS_NAME, 'property-card-link').get_attribute('href'))
        return address_list, price_list, link_list

    def next_page(self):
        listings = self.driver.find_element(By.ID, 'search-page-list-container')
        next_page_link = listings.find_element(By.CSS_SELECTOR, 'a[title="Next page"]')
        next_page_link.click()

    def run(self):
        self.open_webpage()
        addresses = []
        prices = []
        links = []
        for page_number in range(5):
            addresses, prices, links = zs.scrape(addresses, prices, links)
            zs.next_page()
        return addresses, prices, links


if __name__ == '__main__':
    zs = ZillowScraper()
    print(zs.run())

