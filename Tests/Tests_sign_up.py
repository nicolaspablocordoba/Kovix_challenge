import sys
import json
with open("../Data/JSON_DATA_FILE.json") as path_data:
    json_path = json.loads(path_data.read())
sys.path.append(json_path["ABSOLUTE_PATH"])
import inspect
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.Page_objects.Page_object_sign_up import PageObjectSignUp
from src.Functions.Functions_create_data_random import *


TIMEOUT = 10


class TestsSignUP(unittest.TestCase):
    def setUp(self):
        # CHROME CONFIGURATION
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument("--lang=en")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.implicitly_wait(TIMEOUT)

        # JSON lOAD
        with open("../Data/JSON_DATA_FILE.json") as data:
            self.json_data = json.loads(data.read())

        # PAGE OBJECT
        self.sign_up = PageObjectSignUp(self.driver)

        # RANDOM DATA
        self.random_user = create_random_user()
        self.random_password = create_random_password()
        self.random_email = create_random_email()

    def test_sign_up_empty_fields(self):
        """
        2. Prueba el formulario de sign-up
            a. Comienza en la pantalla de sign-up.
            b. Ingresa algunos datos inválidos o campos vacíos.
            c. Enviar formulario.
            d. Verificar que el sistema no te permite completar un formulario sin valores correctos.
        """
        try:

            # a. Comienza en la pantalla de sign-up.
            self.driver.get(self.json_data["URL_SIGN_UP"])
            time.sleep(0.3)
            self.sign_up.click_accept_cookies_button()

            # b. Ingresa algunos datos inválidos o campos vacíos.
            self.sign_up.click_username_field()
            self.sign_up.clear_username_field()

            self.sign_up.click_password_field()
            self.sign_up.clear_username_field()

            self.sign_up.click_password_confirm_field()
            self.sign_up.clear_password_confirm_field()

            # c. Enviar formulario.
            self.sign_up.click_sign_up_button()

        except Exception:
            self.driver.save_screenshot("except_" + inspect.stack()[0][3] + ".png")
            self.assertTrue(False)
        else:
            # ASSERT
            # d. Verificar que el sistema no te permite completar un formulario sin valores correctos.
            self.error_message = WebDriverWait(self.driver, TIMEOUT).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main"]/div/div/div/div/section/div/div/div/a/h2/span'))).text
            self.assertIn("There was an error processing your signup", self.error_message)

    def test_create_account(self):
        """
        a. Comienza en la pantalla de sign-up.
        b. Click sobre campo Username y completar con un usuario aleatorio
        c. Click sobre campo Password y completar con un password aleatorio
        d. Click sobre campo Password Confirm y completar con la misma password del paso anterior aleatorio
        e. Click sobre campo Email y completar con un email aleatorio
        f. Enviar formulario.
        g. Verificar que el sistema no te permite completar un formulario sin valores correctos.
        """
        try:
            # a. Comienza en la pantalla de sign-up.
            self.driver.get(self.json_data["URL_SIGN_UP"])
            time.sleep(0.5)
            self.sign_up.click_accept_cookies_button()

            # b. Click sobre campo Username y completar con un usuario aleatorio
            self.sign_up.click_username_field()
            self.sign_up.clear_username_field()
            self.sign_up.complete_username_field(self.random_user)

            # c. Click sobre campo Password y completar con un password aleatorio
            self.sign_up.click_password_field()
            self.sign_up.clear_password_field()
            self.sign_up.complete_password_field(self.random_password)

            # d. Click sobre campo Password Confirm y completar con la misma password del paso anterior aleatorio
            self.sign_up.click_password_confirm_field()
            self.sign_up.clear_password_confirm_field()
            self.sign_up.complete_password_confirm_field(self.random_password)

            # e. Click sobre campo Email y completar con un email aleatorio
            self.sign_up.click_email_field()
            self.sign_up.clear_email_field()
            self.sign_up.complete_email_field(self.random_email)

            # f. Enviar formulario.
            self.sign_up.click_sign_up_button()

        except Exception:
            self.driver.save_screenshot("except_" + inspect.stack()[0][3] + ".png")
            self.assertTrue(False)

        else:
            # ASSERT
            # g. Verificar que el sistema no te permite completar un formulario sin valores correctos.
            self.account_verification_message = WebDriverWait(self.driver, TIMEOUT).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main"]/section/div/div/div/div/div/a/h2/span'))).text
            self.assertIn("Account verification required", self.account_verification_message)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
