from common.public_untils import EXCEL_PATH1
from common.read_data import rd
from common.read_excel import re


def test():
    a=rd.read_extract_yaml("tiens_token")
    print(a)
    print(type(a))