# coding:gbk
# __author__ = 'LiJuan'
import os
import openpyxl
import pytest
from common.read_data import rd
from common.read_excel import re
from operation.user_operation import assert_validate, get_extract_data, user_order_delivery, check_user_order

BASE_PATH = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
data_file_path = os.path.join(BASE_PATH, "data", "vshare.xlsx")
print(BASE_PATH)




def setup_module():
    global excel, sheet
    excel = openpyxl.load_workbook(data_file_path)
    sheet = excel['info']


class TestUserOrderDelivery():

    @pytest.mark.smoke
    @pytest.mark.parametrize('data', re.read_excel(data_file_path))
    def test_user_order_delivery(self,data):
        r = data[0] + 1
        rd.report_api(data[11],data[17],data[16],data[18],data[19])
        res = user_order_delivery(data[3],data[1],data[2],data[5],data[4],data[7],data[6],data[15])
        assert_validate(excel,sheet,r,res,data[8],data[9],data_file_path)
        get_extract_data(data[12], data[13], res, data[14])
        check_user_order(sheet,excel,data_file_path,r,data[20],data[21])







if __name__ == '__main__':
    pytest.main(['-q','-s', 'test_01_user_order.py'])

