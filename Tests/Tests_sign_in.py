import sys
sys.path.insert(0, '../src')
import json
import inspect
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.Page_objects.Page_object_sign_in import PageObjectSignIn


TIMEOUT = 10


class TestsSignIn(unittest.TestCase):
    def setUp(self):
        # CHROME CONFIGURATION
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.implicitly_wait(TIMEOUT)

        # JSON lOAD
        with open("../Data/JSON_DATA_FILE.json") as data:
            self.json_data = json.loads(data.read())

        # PAGE OBJECT
        self.sign_in = PageObjectSignIn(self.driver)

    def test_login(self):
        """
        3. Prueba el formulario de sign-in
            a. Comienza en la pantalla de sign-in.
            b. Ingresa datos válidos de una cuenta existente.
            c. Enviar formulario.
            d. Verificar que enviar el formulario con datos válidos genera un sign-in.
        """
        try:
            # a. Comienza en la pantalla de sign-in.
            self.driver.get(self.json_data["URL_SIGN_IN"])

            # b. Ingresa datos válidos de una cuenta existente.
            self.sign_in.click_username_field()
            self.sign_in.clear_username_field()
            self.sign_in.complete_username_field(self.json_data["USERNAME"])

            self.sign_in.click_username_field()
            self.sign_in.clear_password_field()
            self.sign_in.complete_password_field(self.json_data["PASSWORD"])

            # c. Enviar formulario.
            self.sign_in.click_login_button()

        except Exception:
            self.driver.save_screenshot("except_" + inspect.stack()[0][3] + ".png")
            self.assertTrue(False)

        else:
            # ASSERT
            # d. Verificar que enviar el formulario con datos válidos genera un sign-in.
            self.url_profile = self.driver.current_url
            self.assertEqual(self.url_profile, 'https://www.themoviedb.org/u/kovix_test')

    def test_login_empty_fields(self):
        """
        a. Comienza en la pantalla de sign-in.
        b. Dejar vacío el campo Username.
        c. Dejar vacío el campo Password
        d. Click sobre el botón login
        d. Verificar mensaje de error
        """
        try:
            # a. Comienza en la pantalla de sign-in.
            self.driver.get(self.json_data["URL_SIGN_IN"])

            # b. Dejar vacío el campo Username.
            self.sign_in.click_username_field()
            self.sign_in.clear_username_field()

            # c. Dejar vacío el campo Password
            self.sign_in.click_password_field()
            self.sign_in.clear_password_field()

            # d. Click sobre el botón login
            self.sign_in.click_login_button()

        except Exception:
            self.driver.save_screenshot("except_" + inspect.stack()[0][3] + ".png")
            self.assertTrue(False)

        else:
            # ASSERT
            # d. Verificar mensaje de error
            self.error_message = WebDriverWait(self.driver, TIMEOUT).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main"]/section/div/div/div/div/div/a/h2/span'))).text
            self.assertIn("There was a problem", self.error_message)

    def test_login_with_incorrect_credentials(self):
        """
        a. Comienza en la pantalla de sign-in.
        b. completar el campo Username con un valor inexistente.
        c. completar el campo Password con un valor inexistente.
        d. Click sobre el botón login
        d. Verificar mensaje de error
        """
        try:
            # a. Comienza en la pantalla de sign-in.
            self.driver.get(self.json_data["URL_SIGN_IN"])

            # b. completar el campo Username con un valor inexistente.
            self.sign_in.click_username_field()
            self.sign_in.clear_username_field()
            self.sign_in.complete_username_field(self.json_data["USERNAME_INCORRECT"])

            # c. completar el campo Password con un valor inexistente.
            self.sign_in.click_password_field()
            self.sign_in.clear_password_field()
            self.sign_in.complete_password_field(self.json_data["PASSWORD_INCORRECT"])

            # d. Click sobre el botón login
            self.sign_in.click_login_button()

        except Exception:
            self.driver.save_screenshot("except_" + inspect.stack()[0][3] + ".png")
            self.assertTrue(False)

        else:
            # ASSERT
            # d. Verificar mensaje de error
            self.error_message = WebDriverWait(self.driver, TIMEOUT).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main"]/section/div/div/div/div/div/a/h2/span'))).text
            self.assertIn("There was a problem", self.error_message)

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
