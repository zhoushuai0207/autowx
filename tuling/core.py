# -*- coding: utf-8 -*-
from wxapp.settings import TULING_TOKEN, TULING_URL
from utils.http import requests_noauth


class TuLingApi(object):

    @classmethod
    def get_text(cls, userid="1", text=""):
        body = {
            "reqType": 0,
            "perception": {
                "inputText": {
                    "text": text
                }
            },
            "userInfo": {
                "apiKey": TULING_TOKEN,
                "userId": userid
            }
        }
        r = requests_noauth("POST", TULING_URL, data=body, timeout=3).json()
        return r["results"][0]["values"]
