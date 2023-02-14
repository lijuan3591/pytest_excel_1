# coding:gbk
# __author__ = 'LiJuan'


import openpyxl
import allure

from common.logger import logger
from common.public_untils import EXCEL_PATH1, EXCEL_PATH


class ReadExcel():
    @allure.step("===>读取excel文件")
    def read_excel(self,path):
        try:
            wb = openpyxl.load_workbook(path)
            sheet = wb['info']

            tup_list = []
            for i in sheet.values:
                if type(i[0]) is int:
                    tup_list.append(i)
            logger.info("tup_list的值是{}".format(tup_list))
            return tup_list
        except Exception as e:
            logger.info(e)
            raise

re = ReadExcel()


if __name__ =='__main__':
    re = ReadExcel()
    a=re.read_excel(EXCEL_PATH)
    print(a[1])
    print(type(a))


