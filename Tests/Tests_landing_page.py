import json
import inspect
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from src.Page_objects.Page_object_landing_page import PageObjectLandingPage


TIMEOUT = 10


class TestsLandingPage(unittest.TestCase):
    def setUp(self):
        # CHROME CONFIGURATION
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.implicitly_wait(TIMEOUT)

        # JSON lOAD
        with open("../Data/JSON_DATA_FILE.json") as netflix_url:
            self.json_data = json.loads(netflix_url.read())

        # PAGE OBJECT
        self.landing_page = PageObjectLandingPage(self.driver)

    def test_search_movie(self):
        """
        1. Probar el buscador de películas
            a. Comienza en la landing page de The Movies Database.
            b. Click en el input para buscar películas.
            c. Escribí el nombre de tu película favorita.
            d. Verifica que el buscador de películas funcione correctamente.
        """
        try:
            # a. Comienza en la landing page de The Movies Database.
            self.driver.get(self.json_data["URL_LANDING_PAGE"])

            # b. Click en el input para buscar películas.
            self.landing_page.click_search_field()
            self.landing_page.clear_search_field()

            # c. Escribí el nombre de tu película favorita.
            self.landing_page.complete_search_field(self.json_data["MOVIE"])
            self.landing_page.click_search_button()

        except Exception:
            self.driver.save_screenshot("except_" + inspect.stack()[0][3] + ".png")
            self.assertTrue(False)

        else:
            # ASSERT
            # d. Verifica que el buscador de películas funcione correctamente.
            self.movie_result = self.driver.find_element(By.XPATH, '//div/div[2]/div[1]/div/div/a/h2').text
            self.assertIn(self.json_data["MOVIE"].lower(), self.movie_result.lower())

    def test_empty_search(self):
        """
        a. Comienza en la landing page de The Movies Database.
        b. Click en el input para buscar películas.
        c. dejar el input de película vacío
        d. Click en el botón de search
        e. Verificar la búsqueda sin resultados
        """
        try:
            # a. Comienza en la landing page de The Movies Database.
            self.driver.get(self.json_data["URL_LANDING_PAGE"])

            # b. Click en el input para buscar películas
            self.landing_page.click_search_field()

            # c. dejar el input de película vacío
            self.landing_page.clear_search_field()

            # d. Click en el botón de search
            self.landing_page.click_search_button()

        except Exception:
            self.driver.save_screenshot("except_" + inspect.stack()[0][3] + ".png")
            self.assertTrue(False)
        else:
            # ASSERT
            # e. Verificar la búsqueda sin resultados
            self.message_result = self.driver.find_element(By.XPATH, '//*[@id="main"]/section/div/div/div[2]/section/div[1]/div/p').text
            self.assertEqual("There are no movies that matched your query.", self.message_result)

    def test_search_movie_with_year_filter(self):
        """
        a. Comienza en la landing page de The Movies Database.
        b. Click en el input para buscar películas.
        c. Completar el input con el filtro de year
        d. Click en el botón de search
        e. Verificar el resultado de la búsqueda
        """
        try:
            # a. Comienza en la landing page de The Movies Database.
            self.driver.get(self.json_data["URL_LANDING_PAGE"])

            # b. Click en el input para buscar películas.
            self.landing_page.click_search_field()
            self.landing_page.clear_search_field()

            # c. Escribí el nombre de tu película favorita.
            self.landing_page.complete_search_field(self.json_data["MOVIE_WITH_YEAR_FILTER"])
            self.landing_page.click_search_button()

        except Exception:
            self.driver.save_screenshot("except_" + inspect.stack()[0][3] + ".png")
            self.assertTrue(False)

        else:
            # ASSERT
            # d. Verifica que el buscador de películas funcione correctamente.
            self.movie_result = self.driver.find_element(By.XPATH, '//div/div[2]/div[1]/div/div/a/h2').text
            self.assertIn(self.movie_result.lower(), self.json_data["MOVIE_WITH_YEAR_FILTER"].lower())

    def tearDown(self):
        self.driver.close()
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
