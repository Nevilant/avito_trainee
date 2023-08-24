from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from locators.locators import ProductLocators


class CardOfProductPage(Base):
    url = 'https://www.avito.ru/nikel/knigi_i_zhurnaly/domain-driven_design_distilled_vaughn_vernon_2639542363'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Getters

    def get_product_name(self):
        return self.driver.find_element(By.CSS_SELECTOR, ProductLocators.PRODUCT_NAME)

    def get_button_add_to_favourite(self):
        return self.driver.find_element(By.CSS_SELECTOR, ProductLocators.BUTTON_ADD_TO_FAVOURITE)

    def get_check_button_on(self):
        return Wait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ProductLocators.IN_FAVOURITE)))

    # Actions

    def click_to_button(self):
        self.get_button_add_to_favourite().click()

    # Methods

    def add_to_favourite(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.assert_words(self.get_product_name(), 'Domain-Driven Design Distilled Vaughn Vernon')
        self.click_to_button()
        self.assert_words(self.get_check_button_on(), 'В избранном')
