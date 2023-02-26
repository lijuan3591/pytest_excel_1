import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
EXCEL_PATH = os.path.join(BASE_PATH, "pytest_excel_1\data", "vshare.xlsx")
EXCEL_PATH1=os.path.join(BASE_PATH, "pytest_excel_1\data", "vshare_scenario.xlsx")
YAML_PATH=os.path.join(BASE_PATH, "pytest_excel_1\\testcases\\api_test")
print(EXCEL_PATH1)
