import os
from core.rest_client import RestClient
from common.read_data import data

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
api_root_url = data.load_ini(data_file_path)["host"]["api_root_url"]
api_root_login_url = data.load_ini(data_file_path)["host"]["api_root_login_url"]


class User(RestClient):
# class User():

    def __init__(self, api_root_url,api_root_login_url, **kwargs):
        super(User, self).__init__(api_root_url,api_root_login_url,**kwargs)

    # def list_all_users(self, **kwargs):
    #     return self.get("/users", **kwargs)
    #
    # def list_one_user(self, username, **kwargs):
    #     return self.get("/users/{}".format(username), **kwargs)
    #
    # def register(self, **kwargs):
    #     return self.post("/register", **kwargs)

    def login(self, url, **kwargs):
        return self.post(url,**kwargs)

    def shoppingcart_add(self, url, **kwargs):
        return self.post(url, **kwargs)

    def get_checkoutid(self,url,**kwargs):
        return  self.post(url,**kwargs)

    def checkout(self, url, **kwargs):
        return self.get(url,**kwargs)

    def select_method(self,url,**kwargs):
        return self.post(url,**kwargs)

    def go_pay(self,url,**kwargs):
        return self.post(url, **kwargs)

    def select_paychannel(self,url,**kwargs):
        return self.get(url, **kwargs)

    def create_order(self,url,**kwargs):
        return self.post(url, **kwargs)

    # def get_checkoutid(self, **kwargs):
    #     return self.post("/order-aggr/api/checkout", **kwargs)
    #
    # def fetch_checkoutid(self, **kwargs):
    #     return self.post("/order-aggr/api/checkout/v2/2022234224046882816", **kwargs)
    #
    # def select_method(self,**kwargs):
    #     return self.post("/order-aggr/api/checkout/select_shipping_method", **kwargs)
    #
    # def go_pay(self,**kwargs):
    #     return self.post("/order-aggr/api/checkout/go_pay", **kwargs)
    #
    # def select_paychannel(self,**kwargs):
    #     return self.post(" / cashier / api / pay_channel / select?goodsorderid = 99812211230001 & language = zh - cn", **kwargs)
    #
    # def create_order(self,**kwargs):
    #     return self.post("/cashier/api/pay/create_order", **kwargs)
    #
    # def query_order(self,**kwargs):
    #     return self.post("/order-aggr/api/order/status/99812211230001", **kwargs)


    # def update(self, user_id, **kwargs):
    #     return self.put("/update/user/{}".format(user_id), **kwargs)
    #
    # def delete(self, name, **kwargs):
    #     return self.post("/delete/user/{}".format(name), **kwargs)



user = User(api_root_url,api_root_login_url)