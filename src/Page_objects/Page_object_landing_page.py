"""El siguiente page object está dirigido a la pantalla de landing page"""

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


TIMEOUT = 10


class PageObjectLandingPage:
    def __init__(self, my_driver):
        self.driver = my_driver

        # landing page
        self.search_field = (By.ID, 'inner_search_v4')
        self.search_button = (By.XPATH, "//input[@type='submit' and @value='Search']")

    # Methods
    def click_search_field(self):
        """This method clicks on the search field"""
        WebDriverWait(self.driver, TIMEOUT).until(EC.element_to_be_clickable(self.search_field)).click()

    def clear_search_field(self):
        """This method cleans the text that may be in the search field"""
        WebDriverWait(self.driver, TIMEOUT).until(EC.element_to_be_clickable(self.search_field)).clear()

    def complete_search_field(self, text):
        """This method receives a text as a parameter and inserts it in the search field"""
        WebDriverWait(self.driver, TIMEOUT).until(EC.element_to_be_clickable(self.search_field)).send_keys(text)

    def click_search_button(self):
        """This method clicks the search button"""
        WebDriverWait(self.driver, TIMEOUT).until(EC.element_to_be_clickable(self.search_button)).click()
