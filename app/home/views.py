# -*- coding:utf-8 -*-

from . import home


@home.route('/', methods=['get'])
def index():
    return "hello world"
