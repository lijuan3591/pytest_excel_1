#coding=utf-8
#coding=gbk
# __author__ = 'LiJuan'

import os
import random
import string
import allure
import yaml
import json
from configparser import ConfigParser
from jsonpath import jsonpath
from common.logger import logger


class MyConfigParser(ConfigParser):
    # 重写 configparser 中的 optionxform 函数，解决 .ini 文件中的 键option 自动转为小写的问题
    def __init__(self, defaults=None):
        ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionstr):
        return optionstr

class ReadFileData():

    def __init__(self):
        pass

    @allure.step("读取ini配置文件")
    def load_ini(self, file_path):
        logger.info("加载 {} 文件......".format(file_path))
        config = MyConfigParser()
        config.read(file_path, encoding="UTF-8")
        data = dict(config._sections)
        # print("读到数据 ==>>  {} ".format(data))
        return data

    @allure.step("读取extract.yaml文件")
    # 读取extract.yaml文件
    def read_extract_yaml(self, key):
        with open(os.getcwd() + "/extract.yml", mode='r', encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value[key]


    @allure.step("抽取数据写入extract.yaml文件")
    # 写入extract.yaml文件
    def write_extract_yaml(self, data):
        with open(os.getcwd() + "/extract.yml", mode='a', encoding='utf-8') as f:
            yaml.dump(data=data, stream=f, allow_unicode=True)

    @allure.step("清除extract.yaml文件")
    # 清除extract.yaml文件
    def clear_extract_yaml(self):
        with open(os.getcwd() + "/extract.yml", mode='w', encoding='utf-8') as f:
            f.truncate()


    @allure.step("===>抽取数据")
    def get_text(self, res, express):
        resp = json.loads(res.text)
        tmp = jsonpath(resp, express)
        logger.info("tmp[0]的值是{}".format(tmp[0]))
        return tmp[0]

    @allure.step("生成随机整数的字符串")
    def get_random(self, n):
        return ''.join(random.sample(string.digits, n))

    @allure.step("生成随机数字和字母的字符串")
    def get_random_sample(self, n):
        return ''.join(random.sample(string.ascii_letters + string.digits, n))

    def report_api(self,title,feature,story,description,severity):
        # 动态获取标题
        if title:
            allure.dynamic.title(title)
        # 动态获取feature模块
        if feature:
            allure.dynamic.feature(feature)
        # 动态获取story模块
        if story:
            allure.dynamic.story(story)
        # 动态获取备注
        if description:
            allure.dynamic.description(description)
        # 动态获取级别
        if severity:
            allure.dynamic.severity(severity)


rd = ReadFileData()



if __name__ == '__main__':

    # print(os.getcwd())
    print(rd.get_random_sample(9))
    print(rd.get_random(9))
    # value = '${get_random_sample(9)}'
    # print(rd.get_oldvalue(value,'${get_random_sample(',')}',20,-2))
