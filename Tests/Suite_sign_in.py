import sys
import json
with open("../Data/JSON_DATA_FILE.json") as path_data:
    json_path = json.loads(path_data.read())
sys.path.append(json_path["ABSOLUTE_PATH"])
import unittest
import xmlrunner


# ARCHIVOS DONDE SE ENCUENTRAN LOS TEST
import Tests.Tests_sign_in

# INSTANCIA DE LOADER Y SUIT
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# AGREGADO DE TESTS A LA SUIT
suite.addTest(Tests.Tests_sign_in.TestsSignIn("test_login"))
suite.addTest(Tests.Tests_sign_in.TestsSignIn("test_login_empty_fields"))
suite.addTest(Tests.Tests_sign_in.TestsSignIn("test_login_with_incorrect_credentials"))

# RUNNER Y REPORTE HTML
testRunner = xmlrunner.XMLTestRunner(output='test-reports').run(suite)
