#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import logging
import time
from django.views import View

from utils.utils import write_file, read_file
from common.wxcore import WxApi

LOG = logging.getLogger(__name__)


class WxBaseView(View):

    def check_valid_token(self, validtime):
        isvalid = False
        if validtime - time.time() > 600:
            isvalid = True
        return isvalid

    def get_token(self, file="/tmp/wxtoken.json"):
        """fiel fmt: {"token":"hello", "valid_time":"xxxxxx"}"""
        try:
            token_json = read_file(file)
            token_json = json.loads(token_json)
            is_valid_token = self.check_valid_token(token_json["valid_time"])
            if is_valid_token:
                return token_json["token"]
            else:
                raise Exception("无效的Token")
        except Exception:
            # IOError没有找到对应的文件
            wdata = {"token": "hello", "valid_time": "xxxxxx"}
            token, expires_in = WxApi.get_token()
            wdata["token"] = token
            wdata["valid_time"] = int(time.time()) + int(expires_in)
            write_file(filename=file, context=json.dumps(wdata))
            return token
