from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC

from locators.locators import FavouritesLocators
from base.base_class import Base


class FavouritesPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Getters

    def get_link_favourites(self):
        return self.driver.find_element(By.CSS_SELECTOR, FavouritesLocators.LINK_FAVOURITES)

    def get_product_name(self):
        return self.driver.find_element(By.CSS_SELECTOR, FavouritesLocators.PRODUCT_NAME)

    # Actions

    def click_to_link_favorites(self):
        self.get_link_favourites().click()

    # Methods

    def check_favourites(self):
        self.click_to_link_favorites()
        self.get_current_url()
        self.assert_words(self.get_product_name(), 'Domain-Driven Design Distilled Vaughn Vernon')

