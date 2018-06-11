#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from django.views import View
from conf import constans as C

LOG = logging.getLogger(__name__)


class TuLingView(View):

    def __init__(self, **kwargs):
        self.r_data = {"msg": "OK", "code": C.CODE_OK}