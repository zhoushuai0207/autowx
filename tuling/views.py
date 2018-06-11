#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from django.http import HttpResponse

from common.baseview import BaseView
from tuling.core import TuLingApi
import yaml


LOG = logging.getLogger(__name__)


class PingHandler(BaseView):
    def get(self, *args, **kwargs):
        """检查服务是否正常使用"""
        return HttpResponse("OK")


class ProxyHandler(BaseView):
    """转发图灵API"""
    def post(self, *args, **kwargs):
        """
        {'Content': 'helloworkd', 'FromUserName': 'xxxx', 'URL': 'http://118.24.117.227/tuling/proxy',
        'MsgId': 1, 'CreateTime': 1528683345, 'ToUserName': 'zs_master', 'MsgType': 'text'}
        :param args:
        :param kwargs:
        :return:
        """
        body = yaml.safe_load(self.request.body)
        r = TuLingApi.get_text(userid=body["FromUserName"], text=body["Content"])
        print(r)
        return HttpResponse("OK")