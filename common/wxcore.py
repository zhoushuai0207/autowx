# -*- coding: utf-8 -*-
from wxapp.settings import WX_URL, WX_APPID, WX_SECRET
from utils.http import requests_noauth


class WxApi(object):

    @classmethod
    def get_token(cls, wx_appid=WX_APPID, wx_secret=WX_SECRET):
        # https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=wx16be51dfaf68d05c&secret=
        # 00f6efa87e7fe2beac844e721cc21702
        url = WX_URL + "/token?" + "&".join(["grant_type=client_credential", "appid=%s" % wx_appid, "secret=%s" % wx_secret])
        r = requests_noauth("GET", url, timeout=3)
        if r.status_code // 100 != 2:
            r = r.json()
            if "access_token" in r:
                return r["access_token"], r["expires_in"]
        raise Exception("Get Token error!")

