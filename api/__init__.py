from api.article import MpArticle, MsQArticle, MsEArticle, AppQArticle
from api.login import MpLogin, MisLogin, AppLogin
from app import basic_logger_config


class FactoryApi:
    mp_login = MpLogin()
    mp_article = MpArticle()
    mis_login= MisLogin()
    mis_query = MsQArticle()
    mis_exam = MsEArticle()
    app_login = AppLogin()
    app_query = AppQArticle()
basic_logger_config()