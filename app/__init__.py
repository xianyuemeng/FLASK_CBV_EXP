# -*- coding:utf-8 -*-

from flask import Flask
import os
from app.api import api, api_views_2

app = Flask(__name__)

# api.register(app)


def register_api(view, endpoint, url, pk='id', pk_type='int'):
    view_func = view.as_view(endpoint)
    app.add_url_rule(url, defaults={pk: None},
                     view_func=view_func, methods=['GET',])
    app.add_url_rule(url, view_func=view_func, methods=['POST',])
    app.add_url_rule('%s<%s:%s>' % (url, pk_type, pk), view_func=view_func,
                     methods=['GET', 'PUT', 'DELETE'])

register_api(api_views_2.UserAPI, 'user_api', '/users/', pk='user_id')

# 配置服务器地址
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 创建秘钥
app.config['SECRET_KEY'] = u'\x1e:\xaf\xacS\xddW>\x97?\xb2\x14 \x14\xab\x9b\xdc\xee\xad\xd6\xd9\xf1\x0b\xd7'