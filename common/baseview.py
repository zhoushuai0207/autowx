#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from conf import constans as C

LOG = logging.getLogger(__name__)


class BaseView(View):

    def __init__(self, **kwargs):
        self.r_data = {"msg": "OK", "code": C.CODE_OK}

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(BaseView, self).dispatch(request, *args, **kwargs)
