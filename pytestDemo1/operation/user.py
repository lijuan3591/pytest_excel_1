import json

from jsonpath import jsonpath

from core.result_base import ResultBase
from api.user import user
from common.logger import logger
from common.read_data import ReadFileData
from core.rest_client import RestClient




def login_user(username, password, login_type, headers, url):
    """
    登录用户
    :param username: 用户名
    :param password: 密码
    :return: 自定义的关键字返回结果 result
    """

    result = ResultBase()
    json_data = {
        "username": username,
        "password": password,
        "login_type": login_type
    }
    header = headers
    url=url
    res = user.login(json=json_data, headers=header, url=url)
    result.response = res
    logger.info("登录用户 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result



def shoppingcart_add(is_point, is_start_package, order_type, qty, sku_id, is_limit, headers, url):
    """
    登录用户
    :param username: 用户名
    :param password: 密码
    :return: 自定义的关键字返回结果 result
    """

    result = ResultBase()
    json_data = {
	"is_point": is_point,
	"is_start_package": is_start_package,
	"order_type": order_type,
	"qty": qty,
	"sku_id": sku_id,
	"is_limit": is_limit
}
    header = headers
    url=url
    res = user.shoppingcart_add(json=json_data, headers=header, url=url)
    result.response = res
    logger.info("登录用户 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def get_checkoutid(order_type,pickup_type,shopping_user_checktype,headers,url):
    result = ResultBase()
    json_data = {
        "order_type": order_type,
        "pickup_type": pickup_type,
        "shopping_user_checktype": shopping_user_checktype
    }
    header = headers
    url = url
    res = user.get_checkoutid(json=json_data,headers=header,url=url)
    result.response = res
    logger.info("登录用户 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def checkout(headers, url):
    result = ResultBase()
    header =headers
    url = url
    res = user.checkout(headers=header,url=url)
    result.response = res
    logger.info("登录用户 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def go_pay(checkout_id,note, headers, url):
    try:
        result = ResultBase()
        header = headers
        url = url
        json_data = {
            "checkout_id": checkout_id,
            "note": note
        }
        res = user.go_pay(json=json_data,headers=header, url=url)
        result.response = res
        logger.info("登录用户 ==>> 返回结果 ==>> {}".format(result.response.text))
        return result
    except Exception as e:
        logger.info("go_pay的报错信息：{}".format(e))


def select_method(shipping_type,shipping_address_id,checkout_id,shipping_id,headers,url):
    result = ResultBase()
    header = headers
    url = url
    json_data = {
        "shipping_type": shipping_type,
        "shipping_address_id": shipping_address_id,
        "checkout_id": checkout_id,
        "shipping_id": shipping_id
    }
    res = user.select_method(json=json_data,headers=header, url=url)
    result.response = res
    logger.info("登录用户 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def select_paychannel(headers,url):
    result = ResultBase()
    header = headers
    url = url
    res = user.select_paychannel(headers=header, url=url)
    result.response = res
    logger.info("登录用户 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result


def create_order(goodsorderid,channel_code,sourcehost,headers,url):
    result = ResultBase()
    header = headers
    url = url
    json_data = {
        "goodsorderid": goodsorderid,
        "channel_code": channel_code,
        "sourcehost": sourcehost
    }
    res = user.create_order(json=json_data,headers=header, url=url)
    result.response = res
    logger.info("登录用户 ==>> 返回结果 ==>> {}".format(result.response.text))
    return result



def assert_validate(except_msg,result,extract):
    """
        断言封装
        :validate: 断言
        :result: 返回结果
        :extract: 取值
       """

    result = json.dumps(result)
    # logger.info("assert--result==>>结果是：{}".format(result))
    assert str(except_msg) in result
    logger.info("assert==>>结果是：断言成功")
    result = json.loads(result)
    if extract and isinstance(extract, dict):
        for key,value in extract.items():
            ReadFileData().write_extract_yaml({str(key): ''.join(jsonpath(result, value))})
            logger.info("提取字段key是：{}，提取的value是：{}".format(key, ''.join(jsonpath(result, value))))
            if str(key) == "url":
                newValue = ''.join(jsonpath(result, value))
                ReadFileData().write_extract_yaml({"tenant_id": str(newValue)[54:72]})
                logger.info("提取字段key--tenant_id是：{}，提取的value是：{}".format(key, str(newValue)[54:72]))
                ReadFileData().write_extract_yaml({"tiens_code": str(newValue)[117:]})
                logger.info("提取字段key--tiens_code：{}，提取的value是：{}".format(key, str(newValue)[117:]))

    else:
        logger.info("extract为空,不需要获取返回值")



