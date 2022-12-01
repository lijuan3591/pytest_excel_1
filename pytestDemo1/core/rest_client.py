import os

import requests
import json as complexjson
from common.logger import logger
from common.read_data import ReadFileData, data



class RestClient():

    def __init__(self,api_root_url,api_root_login_url):
        self.api_root_url = api_root_url
        self.api_root_login_url = api_root_login_url
        self.session = requests.session()

    def get(self, url, **kwargs):
        return self.request(url, "GET", **kwargs)

    def post(self, url, data=None,json=None, **kwargs):
        return self.request(url, "POST", data, json, **kwargs)

    def put(self, url, data=None, **kwargs):
        return self.request(url, "PUT", data, **kwargs)

    def delete(self, url, **kwargs):
        return self.request(url, "DELETE", **kwargs)

    def patch(self, url, data=None, **kwargs):
        return self.request(url, "PATCH", data, **kwargs)

    def request(self,url, method, data=None, json=None, **kwargs):
        headers = dict(**kwargs).get("headers")
        params = dict(**kwargs).get("params")
        files = dict(**kwargs).get("params")
        cookies = dict(**kwargs).get("params")
        # 如果请求url路径中包括${和},则需要做参数提取
        if url == "/idserverhq/public/auth/login":
            url = self.api_root_login_url + url
        else:
            for cs in range(1, str(url).count('${') + 1):
                if '${' in url and '}' in url:
                    startIndex = str(url).find('${')
                    endIndex = str(url).find('}')
                    oldValue = str(url)[int(startIndex):int(endIndex) + 1]
                    newValue = ReadFileData().read_extract_yaml(str(oldValue)[2:-1])
                    url = str(url).replace(oldValue, newValue)
            url = self.api_root_url + url
        # 如果headers不为None,并且为字典类型，则在self.headers中增加请求头
        if headers and isinstance(headers, dict):
            # 如果headers请求参数中中包括${和}, 则需要做参数提取
            for key, value in headers.items():
                if str(value).startswith('${') and str(value).endswith('}'):
                    headers[str(key)] = ReadFileData().read_extract_yaml(str(key))
                else:
                    headers[str(key)] = str(value)
        # 如果json请求参数中中包括${和},则需要做参数提取
        if json and isinstance(json,dict):
            for key,value in json.items():
                if str(value).startswith('${') and str(value).endswith('}'):
                    json[str(key)] = ReadFileData().read_extract_yaml(str(key))
                else:
                    json[str(key)] = str(value)

        self.request_log(url, method, data, json, params, headers, files, cookies)
        if method == "GET":
            return self.session.get(url, **kwargs)
        if method == "POST":
            return self.session.post(url, data,json, **kwargs)
        if method == "PUT":
            if json:
                # PUT 和 PATCH 中没有提供直接使用json参数的方法，因此需要用data来传入
                data = complexjson.dumps(json)
            return self.session.put(url, data, **kwargs)
        if method == "DELETE":
            return self.session.delete(url, **kwargs)
        if method == "PATCH":
            if json:
                data = complexjson.dumps(json)
            return self.session.patch(url, data, **kwargs)




        self.request_log(url, method, data, json, params, headers, files, cookies)
        if method == "GET":
            return self.session.get(url, **kwargs)
        if method == "POST":
            return self.session.post(url, data,json, **kwargs)
        if method == "PUT":
            if json:
                # PUT 和 PATCH 中没有提供直接使用json参数的方法，因此需要用data来传入
                data = complexjson.dumps(json)
            return self.session.put(url, data, **kwargs)
        if method == "DELETE":
            return self.session.delete(url, **kwargs)
        if method == "PATCH":
            if json:
                data = complexjson.dumps(json)
            return self.session.patch(url, data, **kwargs)


    def request_log(self, url, method, data=None, json=None, params=None, headers=None, files=None, cookies=None, **kwargs):
        logger.info("接口请求地址 ==>> {}".format(url))
        logger.info("接口请求方式 ==>> {}".format(method))
        # Python3中，json在做dumps操作时，会将中文转换成unicode编码，因此设置 ensure_ascii=False
        logger.info("接口请求头 ==>> {}".format(complexjson.dumps(headers, indent=4, ensure_ascii=False)))
        logger.info("接口请求 params 参数 ==>> {}".format(complexjson.dumps(params, indent=4, ensure_ascii=False)))
        logger.info("接口请求体 data 参数 ==>> {}".format(complexjson.dumps(data, indent=4, ensure_ascii=False)))
        logger.info("接口请求体 json 参数 ==>> {}".format(complexjson.dumps(json, indent=4, ensure_ascii=False)))
        logger.info("接口上传附件 files 参数 ==>> {}".format(files))
        logger.info("接口 cookies 参数 ==>> {}".format(complexjson.dumps(cookies, indent=4, ensure_ascii=False)))
