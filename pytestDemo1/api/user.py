import os
from core.rest_client import RestClient
from common.read_data import data

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
data_file_path = os.path.join(BASE_PATH, "config", "setting.ini")
api_root_url = data.load_ini(data_file_path)["host"]["api_root_url"]
api_root_login_url = data.load_ini(data_file_path)["host"]["api_root_login_url"]


class User(RestClient):

    def __init__(self, api_root_url,api_root_login_url, **kwargs):
        super(User, self).__init__(api_root_url,api_root_login_url,**kwargs)

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





user = User(api_root_url,api_root_login_url)