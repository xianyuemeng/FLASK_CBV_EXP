# -*- coding:utf-8 -*-
from app.errno import ErrorNo
from . import api
from .. import utils
from ..models import User, db
from flask import jsonify


@api.route('/create_user', methods=['GET', 'POST'])
def create_user():
    params = utils.valid_params()
    print(params)
    if params is None:
        return utils.generate_ret(ErrorNo.INVALID_ARGUMENT)
    try:
        u = User(**params)
        print(u)
        print(123)
        db.session.add(u)
        db.session.commit()
        return utils.generate_ret(ErrorNo.SUCCESS)
    except Exception as e:
        return utils.generate_ret(ErrorNo.INTERNAL_SERVER_ERROR)


@api.route('/list_user', methods=['GET', 'POST'])
def list_user():
    # params = utils.valid_params(da)
    u = User.query.all()
    data = []
    for i in u:
        data.append(i.to_dict())
    return utils.generate_ret(ErrorNo.SUCCESS, data)
    # return jsonify(data)
    # return 'hello ppp'
