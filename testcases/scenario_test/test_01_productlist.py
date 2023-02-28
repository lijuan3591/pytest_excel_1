import os

import openpyxl
import pytest

from common.public_untils import EXCEL_PATH1
from common.read_data import rd
from common.read_excel import re
from operation.user_operation import user_order_delivery, assert_validate, get_extract_data, check_user_order

# PATH=r'D:\pytest_excel_1\data\vshare_scenario.xlsx'
BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
PATH1 = os.path.join(BASE_PATH, "data", "vshare.xlsx")


def setup_module():
    global excel, sheet
    excel = openpyxl.load_workbook(PATH1)
    sheet = excel['info']

class TestProductlist:

    @pytest.mark.parametrize('data',re.read_excel(PATH1))
    def test_productlist(self,data):
        r = data[0] + 1
        rd.report_api(data[11],data[17],data[16],data[18],data[19])
        res = user_order_delivery(data[3],data[1],data[2],data[5],data[4],data[7],data[6],data[15])
        assert_validate(excel,sheet,r,res,data[8],data[9],PATH1)
        get_extract_data(data[12], data[13], res, data[14])
        check_user_order(sheet,excel,PATH1,r,data[20],data[21])

if __name__ == '__main__':
    t=TestProductlist().test_productlist().text
    print(t)
    pytest.main(['-q','-s', 'test_01_productlist.py'])

