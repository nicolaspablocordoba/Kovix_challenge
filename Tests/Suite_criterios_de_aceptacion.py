import sys
import json
with open("../Data/JSON_DATA_FILE.json") as path_data:
    json_path = json.loads(path_data.read())
sys.path.append(json_path["ABSOLUTE_PATH"])
import unittest
import src.Functions.HtmlTestRunner as HtmlTestRunner

# ARCHIVOS DONDE SE ENCUENTRAN LOS TEST
import Tests.Tests_landing_page
import Tests.Tests_sign_up
import Tests.Tests_sign_in

loader = unittest.TestLoader()
suite = unittest.TestSuite()
suite.addTest(Tests.Tests_landing_page.TestsLandingPage("test_search_movie"))
suite.addTest(Tests.Tests_sign_up.TestsSignUP("test_sign_up_empty_fields"))
suite.addTest(Tests.Tests_sign_in.TestsSignIn("test_login"))


# RUNNER Y REPORTE HTML
h = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_name="Reporte Suite Criterios de Aceptación", add_timestamp=False, verbosity=2).run(suite)
