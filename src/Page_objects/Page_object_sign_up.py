"""El siguiente page object está dirigido a la pantalla de sign up"""

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


TIMEOUT = 10


class PageObjectSignUp:
    def __init__(self, my_driver):
        self.driver = my_driver

        # landing page
        self.username_field = (By.ID, 'username')
        self.password_field = (By.ID, 'password')
        self.password_confirm_field = (By.ID, 'password_confirm')
        self.email_field = (By.ID, 'email')
        self.sign_up_button = (By.ID, 'sign_up_button')
        self.accept_cookies_button = (By.ID, 'onetrust-accept-btn-handler')

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

    def click_password_confirm_field(self):
        """This method clicks on the password confirm field"""
        WebDriverWait(self.driver, TIMEOUT).until(EC.element_to_be_clickable(self.password_confirm_field)).click()

    def clear_password_confirm_field(self):
        """This method cleans the text that may be in the password confirm field"""
        WebDriverWait(self.driver, TIMEOUT).until(EC.element_to_be_clickable(self.password_confirm_field)).clear()

    def complete_password_confirm_field(self, text):
        """This method receives a text as a parameter and inserts it in the password confirm field"""
        WebDriverWait(self.driver, TIMEOUT).until(EC.element_to_be_clickable(self.password_confirm_field)).send_keys(text)

    def click_email_field(self):
        """This method clicks on the email field"""
        WebDriverWait(self.driver, TIMEOUT).until(EC.element_to_be_clickable(self.email_field)).click()

    def clear_email_field(self):
        """This method cleans the text that may be in the email field"""
        WebDriverWait(self.driver, TIMEOUT).until(EC.element_to_be_clickable(self.email_field)).clear()

    def complete_email_field(self, text):
        """This method receives a text as a parameter and inserts it in the email field"""
        WebDriverWait(self.driver, TIMEOUT).until(EC.element_to_be_clickable(self.email_field)).send_keys(text)

    def click_sign_up_button(self):
        """This method clicks on the sign-up button"""
        WebDriverWait(self.driver, TIMEOUT).until(EC.element_to_be_clickable(self.sign_up_button)).click()

    def click_accept_cookies_button(self):
        """This method clicks on the accept all cookies button"""
        WebDriverWait(self.driver, TIMEOUT).until(EC.element_to_be_clickable(self.accept_cookies_button)).click()
