import time
import warnings


from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service

from pages.card_of_product_page import CardOfProductPage
from pages.favourite_pages import FavouritesPage


def test_add_to_favourites(set_up):
    warnings.filterwarnings("ignore")
    service = Service(executable_path='/path') # Указать  путь к хромдрайверу
    driver = webdriver.WebDriver(service=service)

    card_of_product = CardOfProductPage(driver)
    card_of_product.add_to_favourite()

    favourites = FavouritesPage(driver)
    favourites.check_favourites()

    driver.quit()
