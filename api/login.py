import logging

import requests

from app import MP_BASE_URL, MP_HEADER, MIS_BASE_URL, MIS_HEADER, APP_BASE_URL, APP_HEADER


class MpLogin:
    def __init__(self):
        self.url = MP_BASE_URL + "/mp/v1_0/authorizations"

    def test_mp_login(self, mobile, code):
        params = {"mobile": mobile,"code": code}

        return requests.post(url=self.url,json=params,headers= MP_HEADER)
class MisLogin:
    def __init__(self):
        self.url = MIS_BASE_URL + "/mis/v1_0/authorizations"
    def test_mis_login(self, username, password):
        logging.info("{}手机用户开始登录".format(username))
        params = {"account":username,"password":password}
        return requests.post(url=self.url , json= params, headers = MIS_HEADER)
class AppLogin:
    def __init__(self):
        self.url = APP_BASE_URL + "/app/v1_0/authorizations"
    def test_app_login(self,mobile,code):
        params = {"mobile": mobile, "code": code}
        return requests.post(url=self.url, json=params,headers=APP_HEADER)
