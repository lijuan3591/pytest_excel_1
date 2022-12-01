import pytest
from testcases.conftest import api_data
from common.read_data import ReadFileData


@pytest.fixture(scope="function")
def testcase_data(request):
    testcase_name = request.function.__name__
    return api_data.get(testcase_name)



@pytest.fixture(scope="session",autouse=True)
def clear_yaml():
    ReadFileData().clear_extract_yaml()