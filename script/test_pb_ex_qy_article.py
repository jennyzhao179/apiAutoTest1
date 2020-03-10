import logging
import time

import pytest

from api import FactoryApi
from app import MP_HEADER, MIS_HEADER, APP_HEADER
from utils.utils_tool import assert_t_f, build_data


class TestPbEmQyArticle:
    article_title = None
    article_id = None

    def test_mp_login(self):
        mobile = "13012345678"
        code = "246810"
        mp_login_response = FactoryApi.mp_login.test_mp_login(mobile, code)
        logging.info("自媒体登录结果返回信息为：{}".format(mp_login_response.json()))
        assert mp_login_response.status_code == 201
        assert mp_login_response.json().get("message") == "OK"
        mp_token = "Bearer " + mp_login_response.json().get("data").get("token")
        MP_HEADER["Authorization"] = mp_token

        print(MP_HEADER)
    @pytest.mark.parametrize("article_title,content,channel_id,status_code,msg",build_data("../data/publish_article.json"))
    def test_publish_article(self,article_title,content,channel_id,status_code,msg):
        TestPbEmQyArticle.article_title = article_title.format(time.strftime("%Y%m%d%H%M%S"))
        content = content.format(time.strftime("%Y%m%d%H%M%S"))
        channel_id = channel_id
        mp_publish_article = FactoryApi.mp_article.test_publish_article(TestPbEmQyArticle.article_title, content, channel_id)

        status_code = mp_publish_article.status_code
        msg = mp_publish_article.json().get("message")
        assert status_code == status_code
        assert msg == msg
        TestPbEmQyArticle.article_id = mp_publish_article.json().get("data").get("id")
    def test_mis_login(self):
        username = "testid"
        password = "testpwd123"
        mis_login_response = FactoryApi.mis_login.test_mis_login(username,password)
        status_code = mis_login_response.status_code
        msg = mis_login_response.json().get("message")
        assert status_code == 201
        assert msg == "OK"
        token = mis_login_response.json().get("data").get("token")
        MIS_HEADER["Authorization"] = "Bearer " + token
        logging.info("更新后的信息头是={}".format(MIS_HEADER))
    def test_mis_query(self):
        title = TestPbEmQyArticle.article_title
        channel = "html"
        mis_query_respons = FactoryApi.mis_query.test_query_article(title,channel)
        # status_code = mis_query_respons.status_code
        # msg = mis_query_respons.json().get("message")
        # assert status_code == 200
        # assert msg == "OK"
        assert_t_f(mis_query_respons,200,"OK")

        assert mis_query_respons.json().get("data").get("articles")[0].get("article_id") ==TestPbEmQyArticle.article_id
    def test_e_article(self):

        mis_e_respons = FactoryApi.mis_exam.test_E_article(TestPbEmQyArticle.article_id)
        assert assert_t_f(mis_e_respons,201,"OK")
    def test_app_login(self):
        mobile = "13012345678"
        code =  "246810"
        app_login_response = FactoryApi.app_login.test_app_login(mobile, code)
        print("请求app登录接口返回结果为", app_login_response.json())
        assert assert_t_f(app_login_response,201,"OK")
        APP_HEADER["Authorization"] ="Bearer " + app_login_response.json().get("data").get("token")
        print("APP_HEAER的值为{}".format(APP_HEADER))
    def test_app_query(self):
        channel_id = 1
        timestamp = int(time.time())
        with_top = 0
        app_query_response = FactoryApi.app_query.test_aq_article(channel_id,timestamp,with_top)
        print("APP查询请求返回结果为",app_query_response.json())
        assert assert_t_f(app_query_response,200,"OK")

