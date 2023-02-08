# coding:gbk
# __author__ = 'LiJuan'

import allure
from common.logger import logger
from common.mysql_operate_order import db
from common.read_data import rd
from api.apikey import ak


@allure.step("===>>���ؽ��")
def step_1(result):
    logger.info("����1 ==>>���ؽ����{}".format(result))



@allure.step("===>���ݽ���")
def user_order_delivery(method,base_url,url,headers,params,json,json_data,ext):
    try:
        logger.info("*************** ��ʼִ������ ***************")
        if '/{}' in url:
            ext = ext.split(';')
            data_dict = {
                    'url': base_url + url.format(rd.read_extract_yaml(ext[0])),
                    'headers': eval(headers),
                    'params': eval(params),
                    json: eval(json_data)
                }
        elif 'goodsorderid' in url:
            ext = ext.split(';')
            data_dict = {
                'url': base_url + url.format(rd.read_extract_yaml(ext[0])),
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

        logger.info("data_dict��ֵ��{}".format(data_dict))
        # ����+���
        res = getattr(ak, method)(**data_dict)
        step_1(res.text)
        # print(res.json())
        logger.info("���ؽ����{}".format(res.text))
        return res
    except Exception as e:
        logger.info("test_user_order_delivery�ı�����Ϣ��{}".format(e))
        raise

@allure.step("===>��ȡ����")
def get_extract_data(extract,expr,res,ext):
    if extract is not None:
        extract = extract.split(';')
        expr = expr.split(';')
        for i in range(len(extract)):
            newValue = rd.get_text(res, expr[i])
            rd.write_extract_yaml({str(extract[i]): str(newValue)})
            logger.info("��ȡ�ֶ�key�ǣ�{}����ȡ��value�ǣ�{}".format(extract[i], newValue))
            # if str(extract[i]) == "url":
            if 'url' in str(extract[i]):
                ext = ext.split(';')
                if ext is not None:
                    rd.write_extract_yaml({ext[0]: str(newValue)[54:72]})
                    logger.info("��ȡ�ֶ�key--tenant_id�ǣ�{}����ȡ��value�ǣ�{}".format(extract[i], str(newValue)[54:72]))
                    rd.write_extract_yaml({ext[1]: str(newValue)[117:]})
                    logger.info("��ȡ�ֶ�key--tiens_code��{}����ȡ��value�ǣ�{}".format(extract[i], str(newValue)[117:]))


@allure.step("===>����")
def assert_validate(excel,sheet,r,res,expr,exp_msg,path):
    try:
        rel_result = rd.get_text(res, expr)
        logger.info("rel_result��ֵ{}".format(rel_result))
        if rel_result == exp_msg:
            sheet.cell(r,11).value = 'ͨ��'
            logger.info('��������ִ�гɹ�')
        else:
            sheet.cell(r, 11).value = 'ʧ��'
            logger.info('��������ִ��ʧ��')
    except Exception as e:
        sheet.cell(r, 11).value = '���ؽ�����󣬻��߱��ʽdata[8]����'
        logger.info("���ؽ�����󣬻��߱��ʽdata[8]����{}".format(e))
        raise
    finally:
        excel.save(path)

@allure.step("===>���ݿ�У��")
def check_user_order(sheet,excel,path,r,sql,gsid):
    if sql is not None:
        sql=sql.format(rd.read_extract_yaml(gsid))
        rep = db.select_db(sql)
        for dis in rep:
            if dis['user_distributor_id'] == rd.read_extract_yaml('distributor_id'):
                sheet.cell(r, 23).value = '���ݿ�У��ͨ��'
                logger.info("���ݿ�У��ͨ��")
            else:
                sheet.cell(r, 23).value = '���ݿ�У��ʧ��'
                logger.info("���ݿ�У��ʧ��")
    excel.save(path)
    logger.info("*************** ����ִ������ ***************")

