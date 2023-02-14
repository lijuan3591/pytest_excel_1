# coding:gbk
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
    # ��д configparser �е� optionxform ��������� .ini �ļ��е� ��option �Զ�תΪСд������
    def __init__(self, defaults=None):
        ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionstr):
        return optionstr

class ReadFileData():

    def __init__(self):
        pass

    @allure.step("��ȡini�����ļ�")
    def load_ini(self, file_path):
        logger.info("���� {} �ļ�......".format(file_path))
        config = MyConfigParser()
        config.read(file_path, encoding="UTF-8")
        data = dict(config._sections)
        # print("�������� ==>>  {} ".format(data))
        return data

    @allure.step("��ȡextract.yaml�ļ�")
    # ��ȡextract.yaml�ļ�
    def read_extract_yaml(self, key):
        with open(os.getcwd() + "/extract.yml", mode='r', encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value[key]


    @allure.step("��ȡ����д��extract.yaml�ļ�")
    # д��extract.yaml�ļ�
    def write_extract_yaml(self, data):
        with open(os.getcwd() + "/extract.yml", mode='a', encoding='utf-8') as f:
            yaml.dump(data=data, stream=f, allow_unicode=True)

    @allure.step("���extract.yaml�ļ�")
    # ���extract.yaml�ļ�
    def clear_extract_yaml(self):
        with open(os.getcwd() + "/extract.yml", mode='w', encoding='utf-8') as f:
            f.truncate()


    @allure.step("===>��ȡ����")
    def get_text(self, res, express):
        resp = json.loads(res.text)
        tmp = jsonpath(resp, express)
        logger.info("tmp[0]��ֵ��{}".format(tmp[0]))
        return tmp[0]

    def report_api(self,title,feature,story,description,severity):
        # ��̬��ȡ����
        if title:
            allure.dynamic.title(title)
        # ��̬��ȡfeatureģ��
        if feature:
            allure.dynamic.feature(feature)
        # ��̬��ȡstoryģ��
        if story:
            allure.dynamic.story(story)
        # ��̬��ȡ��ע
        if description:
            allure.dynamic.description(description)
        # ��̬��ȡ����
        if severity:
            allure.dynamic.severity(severity)


rd = ReadFileData()



if __name__ == '__main__':

    # print(os.getcwd())
    # print(data.get_random_sample(9))
    # print(data.get_random(9))
    value = '${get_random_sample(9)}'
    print(rd.get_oldvalue(value,'${get_random_sample(',')}',20,-2))
