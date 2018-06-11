# -*- coding: utf-8 -*-
from django.conf.urls import url

from tuling.views import *

urlpatterns = [
    # 健康检查
    url(r'^ping', PingHandler.as_view()),

    url(r'^proxy', ProxyHandler.as_view()),
]
