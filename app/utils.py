# -*- coding:utf-8 -*-

from flask import request, current_app, session, jsonify, g
from datetime import datetime, date, timedelta
from app.errno import ErrorNo
import json


def get_params():
    if request.method == 'GET':
        params = request.args
        print(params)
    else:
        params = request.get_json() or {}
        print(params)
    return params


def valid_params(filter={}):
    params = {}
    for key, value in get_params().items():
        params[key] = value
    # print(params)
    # print filter
    for key in filter:
        if key not in params:
            continue
        print(key)
        if filter.get(key) is not None:
            try:
                if filter[key] == date:
                    params[key] = datetime.strptime(str(params[key]), '%Y-%m-%d')
                elif filter[key] == datetime:
                    params[key] = datetime.strptime(str(params[key]), '%Y-%m-%d %H:%M:%S')
                elif filter[key] == str:
                    params[key] = params[key]

                elif filter[key] == list or filter[key] == dict or filter[key] == bool:
                    if not isinstance(params[key], filter.get(key)):
                        params[key] = json.loads(params[key])
                    if isinstance(params[key], filter.get(key)):
                        return None
                else:
                    if not isinstance(params[key], filter.get(key)):
                        params[key] = filter[key](eval(params[key]))
                    if isinstance(params[key], filter.get(key)):
                        return None
            except Exception as e:
                return None

    return params


def generate_ret(errorno, data=None):
    ret = {}
    ret['status'] = ErrorNo.get_error_no(errorno)
    if errorno != ErrorNo.SUCCESS:
        ret['description'] = ErrorNo.get_description(errorno)
        if data is not None:
            ret['detail'] = data
    else:
        ret['result'] = data
    return jsonify(ret)


def datetime2str(d, withTime=True):
    if withTime:
        return d.strftime('%Y-%m-%d %H:%M:%S')
    else:
        return d.strftime('%Y-%m-%d')


def str2datetime(s, withTime=True):
    if withTime:
        return datetime.strptime(s, '%Y-%m-%d %H:%M:%S')
    else:
        return datetime.strptime(s, '%Y-%m-%d')