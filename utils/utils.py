#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs


def write_file(filename, context, mode="w", encoding="utf-8"):
    """
    针对小文件的写入
    :param filename: 文件名
    :param context: 内容
    :param mode:  写文件的模式
    :return:
    """
    with codecs.open(filename, mode, encoding=encoding) as fw:
        fw.write(context)


def read_file(filename, mode="r", encoding="utf-8"):
    """
    针对小文件的读取
    :param filename: 文件名
    :param mode:  读文件的模式
    :return:
    """
    with codecs.open(filename, mode, encoding=encoding) as fr:
        context = fr.read()
    return context