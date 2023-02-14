# coding:gbk
# __author__ = 'LiJuan'
import sys
path='D:\\pytestDemo1\\'
sys.path.append(path)
import os
import pytest


# pytest.main(['./testcases/api_test','-s', '-q','./','--clean-alluredir','--alluredir=temp'])


pytest.main(['./testcases/api_test','-s', '-q','--alluredir','./temp','--clean-alluredir'])
os.system('copy environment.properties temp\environment.properties')
os.system("allure generate temp -c -o reports ")







if __name__ == '__main__':
    # pytest.main(['./testcases/api_test','-s', '-q','./','--clean-alluredir','--alluredir=temp'])
    pytest.main(['./testcases/api_test','-s', '-q','--alluredir','./temp','--clean-alluredir'])
    os.system('copy environment.properties temp\environment.properties')
    os.system("allure generate temp -c -o reports")
    # pytest.main()
    # os.system("allure generate temp -o reports --clean")


