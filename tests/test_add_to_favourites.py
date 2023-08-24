import time

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service

from pages.card_of_product_page import CardOfProductPage


def test_add_to_favourites():
    service = Service(executable_path='/home/nevi/Documents/utilities/chromedriver-linux64/chromedriver')
    driver = webdriver.WebDriver(service=service)

    card_of_product = CardOfProductPage(driver)
    card_of_product.add_to_favourite()

    time.sleep(5)
    driver.quit()


