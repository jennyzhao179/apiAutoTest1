import requests

from app import MP_BASE_URL, MP_HEADER, MIS_BASE_URL, MIS_HEADER, APP_BASE_URL, APP_HEADER


class MpArticle:
    def __init__(self):
        self.url = MP_BASE_URL + "/mp/v1_0/articles"

    def test_publish_article(self, title, content, channel_id):
        params = {"title": title, "content": content, "channel_id": channel_id, "cover": {"type": 0, "images": []}}
        return requests.post(url=self.url, json=params, headers=MP_HEADER)
class MsQArticle:
    def __init__(self):
        self.url = MIS_BASE_URL+ "/mis/v1_0/articles"
    def test_query_article(self, title, channel):
        params = {"title":title,"channel":channel}
        return requests.get(url=self.url, params=params,headers=MIS_HEADER)
class MsEArticle:
    def __init__(self):
        self.url = MIS_BASE_URL+"/mis/v1_0/articles"
    def test_E_article(self,id):
        params = {"article_ids": id, "status": 2}
        return requests.put(url=self.url,json=params,headers=MIS_HEADER)
class AppQArticle:
    def __init__(self):
        self.url = APP_BASE_URL+ "/app/v1_1/articles"
    def test_aq_article(self,channel_id ,timestamp, with_top):
        params = {"channel_id" :channel_id,"timestamp":timestamp,"with_top":with_top}
        return requests.get(url=self.url, params=params, headers=APP_HEADER)


