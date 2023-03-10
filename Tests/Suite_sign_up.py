import sys
import json
with open("../Data/JSON_DATA_FILE.json") as path_data:
    json_path = json.loads(path_data.read())
sys.path.append(json_path["ABSOLUTE_PATH"])
import unittest
import src.Functions.HtmlTestRunner as HtmlTestRunner

# ARCHIVOS DONDE SE ENCUENTRAN LOS TEST
import Tests.Tests_sign_up

# INSTANCIA DE LOADER Y SUIT
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# AGREGADO DE TESTS A LA SUIT
suite.addTest(Tests.Tests_sign_up.TestsSignUP("test_sign_up_empty_fields"))
suite.addTest(Tests.Tests_sign_up.TestsSignUP("test_create_account"))


# RUNNER Y REPORTE HTML
h = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_name="Reporte Suite Sign Up", add_timestamp=False, verbosity=2).run(suite)
