import json

from jsonpath import jsonpath

from core.result_base import ResultBase
from api.user import user
from common.logger import logger
from common.read_data import ReadFileData
from core.rest_client import RestClient




#
# def get_all_user_info():
#     """
#     获取全部用户信息
#     :return: 自定义的关键字返回结果 result
#     """
#     result = ResultBase()
#     res = user.list_all_users()
#     result.success = False
#     if res.json()["code"] == 0:
#         result.success = True
#     else:
#         result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["msg"])
#     result.msg = res.json()["msg"]
#     result.response = res
#     return result
#
#
# def get_one_user_info(username):
#     """
#     获取单个用户信息
#     :param username:  用户名
#     :return: 自定义的关键字返回结果 result
#     """
#     result = ResultBase()
#     res = user.list_one_user(username)
#     result.success = False
#     if res.json()["code"] == 0:
#         result.success = True
#     else:
#         result.error = "查询用户 ==>> 接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["msg"])
#     result.msg = res.json()["msg"]
#     result.response = res
#     logger.info("查看单个用户 ==>> 返回结果 ==>> {}".format(result.response.text))
#     return result
#
#
# def register_user(username, password, telephone, sex="", address=""):
#     """
#     注册用户信息
#     :param username: 用户名
#     :param password: 密码
#     :param telephone: 手机号
#     :param sex: 性别
#     :param address: 联系地址
#     :return: 自定义的关键字返回结果 result
#     """
#     result = ResultBase()
#     json_data = {
#         "username": username,
#         "password": password,
#         "sex": sex,
#         "telephone": telephone,
#         "address": address
#     }
#     header = {
#         "Content-Type": "application/json"
#     }
#     res = user.register(json=json_data, headers=header)
#     result.success = False
#     if res.json()["code"] == 0:
#         result.success = True
#     else:
#         result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["msg"])
#     result.msg = res.json()["msg"]
#     result.response = res
#     logger.info("注册用户 ==>> 返回结果 ==>> {}".format(result.response.text))
#     return result
#

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





# def update_user(id, admin_user, new_password, new_telephone, token, new_sex="", new_address=""):
#     """
#     根据用户ID，修改用户信息
#     :param id: 用户ID
#     :param admin_user: 当前操作的管理员用户
#     :param new_password: 新密码
#     :param new_telephone: 新手机号
#     :param token: 当前管理员用户的token
#     :param new_sex: 新性别
#     :param new_address: 新联系地址
#     :return: 自定义的关键字返回结果 result
#     """
#     result = ResultBase()
#     header = {
#         "Content-Type": "application/json"
#     }
#     json_data = {
#         "admin_user": admin_user,
#         "password": new_password,
#         "token": token,
#         "sex": new_sex,
#         "telephone": new_telephone,
#         "address": new_address
#     }
#     res = user.update(id, json=json_data, headers=header)
#     result.success = False
#     if res.json()["code"] == 0:
#         result.success = True
#     else:
#         result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["msg"])
#     result.msg = res.json()["msg"]
#     result.response = res
#     logger.info("修改用户 ==>> 返回结果 ==>> {}".format(result.response.text))
#     return result
#
#
# def delete_user(username, admin_user, token):
#     """
#     根据用户名，删除用户信息
#     :param username: 用户名
#     :param admin_user: 当前操作的管理员用户
#     :param token: 当前管理员用户的token
#     :return: 自定义的关键字返回结果 result
#     """
#     result = ResultBase()
#     json_data = {
#         "admin_user": admin_user,
#         "token": token,
#     }
#     header = {
#         "Content-Type": "application/json"
#     }
#     res = user.delete(username, json=json_data, headers=header)
#     result.success = False
#     if res.json()["code"] == 0:
#         result.success = True
#     else:
#         result.error = "接口返回码是 【 {} 】, 返回信息：{} ".format(res.json()["code"], res.json()["msg"])
#     result.msg = res.json()["msg"]
#     result.response = res
#     logger.info("删除用户 ==>> 返回结果 ==>> {}".format(result.response.text))
#     return result

# if __name__ == '__main__':
#     validate = [{'eq': {'code': 10000}}]
#     extract = {'token': 'token', 'user_id': 'user_id'}
#
#     # caseinfo={'name': '获得统一的鉴权码token', 'request': {'method': 'post', 'url': '/idserverhq/public/auth/login', 'data': {'login_type': 1, 'username': 1532341, 'password': '111111a'}, 'headers': {'select_nation_id': 'RU', 'Content-Type': 'application/json'}}, 'extract': {'token': 'token', 'user_id': 'user_id'}, 'validate': [{'eq': {'code': 10000}}]}
#     result={"code":10000,"msg":"","data":{"token":"EURgFVnQviSLcW-R_QvdvL-1y5E=","modify_password_type":2,"user_info":{"user_ds_info":{"cust_type":0,"is_for_register":1,"real_cust_type":0,"xj":3,"lj_tzpv":0.0000,"lj_tzbv":0.0000,"lj_bv":3978,"lj_pv":4074,"rx_xj":0,"fz_xj":0,"lecturer_level":0},"user_profile_info":{"shop_id":"RU988013","payment_password":"d41d8cd98f00b204e9800998ecf8427e","user_id":"1977280175744286720","user_id_l":1977280175744286720,"distributor_id":"1532117","distributor_name":"Jckcjn Hdjjd","sponsor_id":"89153554","sponsor_name":"NAGA SUGARA","distributor_country":"RU","head_url":"https://dev-res.tiens.com/pocket/avatar/0.png","yx_accid":"44e3e301639d4887a121eeda6e9e5148","yx_token":"9a1661b169b2b2c5f839aeaa7c63253f","mobile":"00079555874448","nick_name":"Shus","invite_code":"","sex":0,"birth":"","email":"737383773@qq.com","user_type":2,"user_level":10,"country_code":"RU","language_id":"zh-cn","enable":1,"introduction":"","mobile_active":1,"attribute":"0","cur_period":"202210","cur_week":"20221004"}}}
#     assert_validate(validate,result,extract)