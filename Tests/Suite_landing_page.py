import sys
import json
with open("../Data/JSON_DATA_FILE.json") as path_data:
    json_path = json.loads(path_data.read())
sys.path.append(json_path["ABSOLUTE_PATH"])
import unittest
import src.Functions.HtmlTestRunner as HtmlTestRunner

# ARCHIVOS DONDE SE ENCUENTRAN LOS TEST
import Tests.Tests_landing_page


# INSTANCIA DE LOADER Y SUIT
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# AGREGADO DE TESTS A LA SUIT
suite.addTest(Tests.Tests_landing_page.TestsLandingPage("test_search_movie"))
suite.addTest(Tests.Tests_landing_page.TestsLandingPage("test_empty_search"))
suite.addTest(Tests.Tests_landing_page.TestsLandingPage("test_search_movie_with_year_filter"))
suite.addTest(Tests.Tests_landing_page.TestsLandingPage("test_landing_page_fail_report"))
suite.addTest(Tests.Tests_landing_page.TestsLandingPage("test_landing_page_error_report"))
suite.addTest(Tests.Tests_landing_page.TestsLandingPage("test_landing_page_skip_report"))


# RUNNER Y REPORTE HTML
h = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_name="Reporte Suite Landing Page", add_timestamp=False, verbosity=2).run(suite)
