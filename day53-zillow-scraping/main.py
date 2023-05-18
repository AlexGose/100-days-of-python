from google_form import GoogleForm
from zillow_scraper import ZillowScraper

if __name__ == '__main__':
    zs = ZillowScraper()
    zs.run()
    print(zs.addresses, zs.prices, zs.links)
    gf = GoogleForm(zs.addresses, zs.prices, zs.links)
    gf.submit_data()
