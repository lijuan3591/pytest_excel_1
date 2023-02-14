# coding:gbk
# __author__ = 'LiJuan'

import allure
from common.logger import logger
# from common.mysql_operate_order import db
from common.read_data import rd
from api.apikey import ak


@allure.step("===>>返回结果")
def step_1(result):
    logger.info("步骤1 ==>>返回结果：{}".format(result))



@allure.step("===>数据解析")
def user_order_delivery(method,base_url,url,headers,params,json,json_data):
    try:
        logger.info("*************** 开始执行用例 ***************")
        if '/{}' in url:
            data_dict = {
                    'url': base_url + url.format(rd.read_extract_yaml('checkout_id')),
                    'headers': eval(headers),
                    'params': eval(params),
                    json: eval(json_data)
                }
        elif 'goodsorderid' in url:
            data_dict = {
                'url': base_url + url.format(rd.read_extract_yaml('goodsorderid')),
                'headers': eval(headers),
                'params': eval(params),
                json: eval(json_data)
            }
        else:
            data_dict = {
                'url': base_url + url,
                'headers': eval(headers),
                'params': eval(params),
                json: eval(json_data)
            }
        logger.info("data_dict的值是{}".format(data_dict))
        # 反射+解包
        res = getattr(ak, method)(**data_dict)
        step_1(res.text)
        logger.info("返回结果是{}".format(res.text))
        return res
    except Exception as e:
        logger.info("test_user_order_delivery的报错信息：{}".format(e))
        raise

@allure.step("===>抽取数据")
def get_extract_data(extract,expr,res):
    if extract is not None:
        extract = extract.split(';')
        expr = expr.split(';')
        for i in range(len(extract)):
            newValue = rd.get_text(res, expr[i])
            rd.write_extract_yaml({str(extract[i]): str(newValue)})
            logger.info("提取字段key是：{}，提取的value是：{}".format(extract[i], newValue))
            if str(extract[i]) == "url":
                rd.write_extract_yaml({"tenant_id": str(newValue)[54:72]})
                logger.info("提取字段key--tenant_id是：{}，提取的value是：{}".format(extract[i], str(newValue)[54:72]))
                rd.write_extract_yaml({"tiens_code": str(newValue)[117:]})
                logger.info("提取字段key--tiens_code：{}，提取的value是：{}".format(extract[i], str(newValue)[117:]))


@allure.step("===>断言")
def assert_validate(excel,sheet,r,res,expr,exp_msg,path):
    try:
        rel_result = rd.get_text(res, expr)
        logger.info("rel_result的值{}".format(rel_result))
        if rel_result == exp_msg:
            sheet.cell(r,11).value = '通过'
            logger.info('测试用例执行成功')
        else:
            sheet.cell(r, 11).value = '失败'
            logger.info('测试用例执行失败')
    except Exception as e:
        sheet.cell(r, 11).value = '返回结果错误，或者表达式data[8]错误'
        logger.info("返回结果错误，或者表达式data[8]错误，{}".format(e))
        raise
    finally:
        excel.save(path)

# @allure.step("===>数据库校验")
# def check_user_order(sheet,excel,path,r,sql,gsid):
#     if sql is not None:
#         sql=sql.format(rd.read_extract_yaml(gsid))
#         rep = db.select_db(sql)
#         for dis in rep:
#             if dis['user_distributor_id'] == rd.read_extract_yaml('distributor_id'):
#                 sheet.cell(r, 23).value = '数据库校验通过'
#                 logger.info("数据库校验通过")
#             else:
#                 sheet.cell(r, 23).value = '数据库校验失败'
#                 logger.info("数据库校验失败")
#     excel.save(path)
#     logger.info("*************** 结束执行用例 ***************")

