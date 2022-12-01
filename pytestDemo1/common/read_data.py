import os

import yaml
import json
from configparser import ConfigParser
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

    def load_yaml(self, file_path):
        logger.info("加载 {} 文件......".format(file_path))
        with open(file_path, encoding='utf-8') as f:
            data = yaml.safe_load(f)
        logger.info("读到数据 ==>>  {} ".format(data))
        return data

    def load_json(self, file_path):
        logger.info("加载 {} 文件......".format(file_path))
        with open(file_path, encoding='utf-8') as f:
            data = json.load(f)
        logger.info("读到数据 ==>>  {} ".format(data))
        return data

    def load_ini(self, file_path):
        logger.info("加载 {} 文件......".format(file_path))
        config = MyConfigParser()
        config.read(file_path, encoding="UTF-8")
        data = dict(config._sections)
        # print("读到数据 ==>>  {} ".format(data))
        return data

    # 读取extract.yaml文件
    def read_extract_yaml(self, key):
        with open(os.getcwd() + "/extract.yml", mode='r', encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value[key]

    # 写入extract.yaml文件
    def write_extract_yaml(self, data):
        with open(os.getcwd() + "/extract.yml", mode='a', encoding='utf-8') as f:
            yaml.dump(data=data, stream=f, allow_unicode=True)

    # 清除extract.yaml文件
    def clear_extract_yaml(self):
        with open(os.getcwd() + "/extract.yml", mode='w', encoding='utf-8') as f:
            f.truncate()

    # 读取yml文件
    def read_testcase_yaml(self, yaml_name):
        with open(os.getcwd() + "\\data\\" + yaml_name, mode='r', encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)
            return value

    def read_data_yaml(self, file_path):
        logger.info("加载 {} 文件......".format(file_path))
        with open(file_path,mode='r', encoding='gbk') as f:
            data = yaml.load(stream=f, Loader=yaml.FullLoader)
        logger.info("读到数据 ==>>  {} ".format(data))
        return data

data = ReadFileData()

if __name__ == '__main__':
    print(os.getcwd())