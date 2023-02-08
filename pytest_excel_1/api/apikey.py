# coding:gbk
# __author__ = 'LiJuan'
import json
import os

import allure
import requests
import yaml
from jsonpath import jsonpath
import allure
from common.logger import logger


class ApiKey():
    @allure.step("发送get请求")
    def get(self,url,params=None,**kwargs):
        return requests.get(url=url,params=params,**kwargs)

    @allure.step("发送post请求")
    def post(self,url,data=None,json=None,**kwargs):
        return requests.post(url,data=data,json=json,**kwargs)


ak = ApiKey()