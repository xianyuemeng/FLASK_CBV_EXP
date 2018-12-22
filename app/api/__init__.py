# -*- coding:utf-8 -*-

from flask import Blueprint

api = Blueprint("api", __name__)
api2 = Blueprint("api2", __name__)
from . import api_views, api_views_2


def register(app):
    app.register_blueprint(api, url_prefix='/api')
    app.register_blueprint(api2, url_prefix='/api2')
