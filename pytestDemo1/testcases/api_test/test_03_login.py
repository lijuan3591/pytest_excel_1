import pytest
import allure
from jsonpath import jsonpath

from operation.user import login_user, assert_validate, shoppingcart_add, get_checkoutid, checkout, select_method, \
    go_pay, select_paychannel, create_order
# from operation.user import assert_validate
from testcases.conftest import api_data
from common.read_data import ReadFileData
from common.logger import logger


@allure.step("步骤1 ==>> 登录用户")
def step_1(username):
    logger.info("步骤1 ==>> 登录用户：{}".format(username))


@allure.severity(allure.severity_level.NORMAL)
@allure.epic("test01_VShare主流程的接口测试")
@allure.feature("test01主流程--选择发运方式为快递下单")
class TestUserOrder():

    @allure.story("test01用例--登录用户")
    @allure.description("该用例是针对获取用户登录接口的测试")
    @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    @allure.title("测试数据：【 {username}，{password}，{except_result}，{except_code}，{except_msg},{headers},{url},{extract}】")
    @pytest.mark.single
    @pytest.mark.smoke
    @pytest.mark.parametrize("username, password, login_type, except_code, except_msg, headers, url,extract",
                             api_data["test_login_user"])

    def test_login_user(self, username, password, login_type, except_code, except_msg,headers,url,extract):
        logger.info("*************** 开始执行**用户登录**用例 ***************")
        result = login_user(username, password, login_type,headers,url)
        step_1(username)

        result = result.response.json()
        # assert result.response.status_code == 200
        logger.info("result==>>结果是：{}".format(result))
        logger.info("except_msg==>>结果是：{}".format(except_msg))
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.get("code")))

        assert_validate(except_msg,result,extract)
        # assert result.response.json().get("code") == except_code
        # assert except_msg in result.response.text
        logger.info("*************** 结束执行**用户登录**用例 ***************")

    @allure.story("test02用例--商品加入购物车")
    @allure.description("该用例是用户登录成功后，将商品加入购物车")
    @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    @allure.title("测试数据：【 {is_point}，{is_start_package}，{order_type}，{qty}，{sku_id}，{is_limit}，{except_code}，{except_msg}，{headers}，{url},{extract}】")
    # @allure.title("测试数据：【 {order_type}，{pickup_type}，{shopping_user_checktype}，{except_code}，{except_msg},{headers},{url},{extract}】")
    @pytest.mark.single
    @pytest.mark.smoke
    @pytest.mark.parametrize("is_point, is_start_package, order_type, qty, sku_id, is_limit,except_code, except_msg,headers, url,extract",
                             api_data["test_shoppingcart_add"])
    def test_shoppingcart_add(self, is_point, is_start_package, order_type, qty, sku_id, is_limit,except_code, except_msg,headers, url,extract):
        logger.info("*************** 开始执行**商品加购**用例 ***************")
        result = shoppingcart_add(is_point, is_start_package, order_type, qty, sku_id, is_limit, headers, url)
        step_1(sku_id)
        result = result.response.json()
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.get("code")))
        assert_validate(except_msg, result, extract)
        logger.info("*************** 结束执行**商品加购**用例 ***************")



    @allure.story("test03用例--获取购物车生成的checkoutID")
    @allure.description("该用例是用户登录成功后，获取购物车生成的checkoutID")
    @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    @allure.title("测试数据：【 {order_type}，{pickup_type}，{shopping_user_checktype}，{except_code}，{except_msg},{headers},{url},{extract}】")
    @pytest.mark.single
    @pytest.mark.smoke
    @pytest.mark.parametrize(
        "order_type,pickup_type,shopping_user_checktype,except_code, except_msg, headers, url, extract",
        api_data["test_get_checkoutid"])
    def test_get_checkoutid(self, order_type, pickup_type, shopping_user_checktype, except_code, except_msg, headers, url, extract):
        logger.info("*************** 开始执行**获取checkoutID**用例 ***************")
        result = get_checkoutid(order_type, pickup_type, shopping_user_checktype, headers, url)
        step_1(url)
        result = result.response.json()
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.get("code")))
        assert_validate(except_msg, result, extract)
        logger.info("*************** 结束执行**获取checkoutID**用例 ***************")


    @allure.story("test04用例--进入到结算页")
    @allure.description("该用例是用户登录成功后，进入到结算页")
    @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    @allure.title("测试数据：【 {except_code}，{except_msg}，{headers}，{url}，{extract}】")
    @pytest.mark.single
    @pytest.mark.smoke
    @pytest.mark.parametrize("except_code, except_msg, headers, url, extract",api_data["test_checkout"])
    def test_checkout(self, except_code, except_msg, headers, url, extract):
        logger.info("*************** 开始执行**进入结算页**用例 ***************")
        result = checkout(headers, url)
        step_1(url)
        result = result.response.json()
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.get("code")))
        assert_validate(except_msg, result, extract)
        logger.info("*************** 结束执行**进入结算页**用例 ***************")


    @allure.story("test05用例--选择发运方式--快递")
    @allure.description("该用例是用户登录成功后，选择发运方式--快递")
    @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    @allure.title("测试数据：【 {shipping_type}，{shipping_address_id}，{checkout_id}，{shipping_id}，{except_code},{except_msg},{headers},{url},{extract}】")
    @pytest.mark.single
    @pytest.mark.smoke
    @pytest.mark.parametrize("shipping_type,shipping_address_id,checkout_id,shipping_id,except_code, except_msg, headers, url, extract",api_data["test_select_method"])
    def test_select_method(self, shipping_type,shipping_address_id,checkout_id,shipping_id,except_code, except_msg, headers, url, extract):
        logger.info("*************** 开始执行**选择发运方式**用例 ***************")
        result = select_method(shipping_type,shipping_address_id,checkout_id,shipping_id,headers,url)
        step_1(url)
        result = result.response.json()
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.get("code")))
        assert_validate(except_msg, result, extract)
        logger.info("*************** 结束**选择发运方式**用例 ***************")



    @allure.story("test06用例--结算页跳转收银台")
    @allure.description("该用例是用户登录成功后，结算页跳转收银台")
    @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    @allure.title("测试数据：【 {checkout_id}，{note}，{except_code}，{except_msg}，{headers},{url},{extract}】")
    @pytest.mark.single
    @pytest.mark.smoke
    @pytest.mark.parametrize("checkout_id,note,except_code, except_msg, headers, url, extract",api_data["test_go_pay"])
    def test_go_pay(self, checkout_id, note, except_code, except_msg, headers, url, extract):
        logger.info("*************** 开始执行**结算页跳转收银台**用例 ***************")
        result = go_pay(checkout_id, note, headers, url)
        step_1(url)
        result = result.response.json()
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.get("code")))
        assert_validate(except_msg, result, extract)
        logger.info("*************** 结束执行**结算页跳转收银台**用例 ***************")

    @allure.story("test07用例--选择支付渠道")
    @allure.description("该用例是用户登录成功后，选择支付渠道")
    @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    @allure.title("测试数据：【 {except_code}，{except_msg}，{headers}，{url}，{extract}】")
    @pytest.mark.single
    @pytest.mark.smoke
    @pytest.mark.parametrize("except_code, except_msg, headers, url, extract",api_data["test_select_paychannel"])
    def test_select_paychannel(self, except_code, except_msg, headers, url, extract):
        logger.info("*************** 开始执行**选择支付渠道**用例 ***************")
        result = select_paychannel(headers, url)
        step_1(url)
        result = result.response.json()
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, 10000))
        assert_validate(except_msg, result, extract)
        logger.info("*************** 结束执行**选择支付渠道**用例 ***************")



    @allure.story("test08用例--创建订单")
    @allure.description("该用例是用户登录成功后，创建订单")
    @allure.issue("https://www.cnblogs.com/wintest", name="点击，跳转到对应BUG的链接地址")
    @allure.testcase("https://www.cnblogs.com/wintest", name="点击，跳转到对应用例的链接地址")
    @allure.title("测试数据：【 {goodsorderid}，{channel_code}，{sourcehost}，{except_code}，{except_msg},{headers},{url},{extract}】")
    @pytest.mark.single
    @pytest.mark.smoke
    @pytest.mark.usefixtures("select_user_order")
    @pytest.mark.parametrize("goodsorderid,channel_code,sourcehost,except_code, except_msg, headers, url, extract",api_data["test_create_order"])
    def test_create_order(self, goodsorderid,channel_code,sourcehost,except_code, except_msg, headers, url, extract):
        logger.info("*************** 开始执行**创建订单**用例 ***************")
        result = create_order(goodsorderid,channel_code,sourcehost,headers, url)
        step_1(url)
        result = result.response.json()
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, 10000))
        assert_validate(except_msg, result, extract)
        logger.info("*************** 结束执行**创建订单**用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_03_login.py"])
