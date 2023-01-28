"""El siguiente page object está dirigido a la pantalla de sign in/login page"""

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


TIMEOUT = 10


class PageObjectSignIn:
    def __init__(self, my_driver):
        self.driver = my_driver

        # landing page
        self.username_field = (By.ID, 'username')
        self.password_field = (By.ID, 'password')
        self.login_button = (By.ID, 'login_button')

    # Methods
    def click_username_field(self):
        """This method clicks on the username field"""
        WebDriverWait(self.driver, TIMEOUT).until(EC.element_to_be_clickable(self.username_field)).click()

    def clear_username_field(self):
        """This method cleans the text that may be in the username field"""
        WebDriverWait(self.driver, TIMEOUT).until(EC.element_to_be_clickable(self.username_field)).clear()

    def complete_username_field(self, text):
        """This method receives a text as a parameter and inserts it in the username field"""
        WebDriverWait(self.driver, TIMEOUT).until(EC.element_to_be_clickable(self.username_field)).send_keys(text)

    def click_password_field(self):
        """This method clicks on the password field"""
        WebDriverWait(self.driver, TIMEOUT).until(EC.element_to_be_clickable(self.password_field)).click()

    def clear_password_field(self):
        """This method cleans the text that may be in the password field"""
        WebDriverWait(self.driver, TIMEOUT).until(EC.element_to_be_clickable(self.password_field)).clear()

    def complete_password_field(self, text):
        """This method receives a text as a parameter and inserts it in the password field"""
        WebDriverWait(self.driver, TIMEOUT).until(EC.element_to_be_clickable(self.password_field)).send_keys(text)

    def click_login_button(self):
        """This method clicks the login button"""
        WebDriverWait(self.driver, TIMEOUT).until(EC.element_to_be_clickable(self.login_button)).click()