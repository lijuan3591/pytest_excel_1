# coding:gbk
import allure
import pytest
from common.read_data import rd


# @pytest.fixture(scope="function")
# def testcase_data(request):
#     testcase_name = request.function.__name__
#     return api_data.get(testcase_name)


@allure.step("步骤前置==>> 数据清理")
@pytest.fixture(scope="session",autouse=True)
def clear_yaml():
    rd.clear_extract_yaml()