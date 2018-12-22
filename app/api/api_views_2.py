# -*- coding:utf-8 -*-

from flask.views import MethodView
from app.errno import ErrorNo
from . import api
from .. import utils
from ..models import User, db


# CBV的一套CRUD
class UserAPI(MethodView):

    def get(self, user_id):
        """

        :param user_id:
        :return:
        """
        if user_id is None:
            # return a list of users
            u = User.query.all()
            data = []
            for i in u:
                data.append(i.to_dict())
            return utils.generate_ret(ErrorNo.SUCCESS, data)
        else:
            # expose a single user
            params = utils.valid_params()
            if params is None:
                return utils.generate_ret(ErrorNo.INVALID_ARGUMENT)
            tmpUser = User.query.filter_by(id=user_id).first()
            if tmpUser:
                return utils.generate_ret(ErrorNo.SUCCESS, tmpUser.to_dict())
            else:
                return utils.generate_ret(ErrorNo.OBJECT_NOT_EXIST)

    def post(self):
        """

        :return:
        """
        # create a new user
        params = utils.valid_params()
        if params is None:
            return utils.generate_ret(ErrorNo.INVALID_ARGUMENT)
        try:
            u = User(**params)
            print(123)
            db.session.add(u)
            db.session.commit()
            return utils.generate_ret(ErrorNo.SUCCESS)
        except Exception as e:
            return utils.generate_ret(ErrorNo.INTERNAL_SERVER_ERROR)

    def delete(self, user_id):
        """
        先做物理删除
        :param user_id:
        :return:
        """
        # delete a single user
        params = utils.valid_params()
        if params is None:
            return utils.generate_ret(ErrorNo.INVALID_ARGUMENT)
        tmpUser = User.query.filter_by(id=user_id).first()
        if tmpUser:
            db.session.delete(tmpUser)
            db.session.commit()
            return utils.generate_ret(ErrorNo.SUCCESS)
        else:
            return utils.generate_ret(ErrorNo.OBJECT_NOT_EXIST)

    def put(self, user_id):
        """
        测试: 修改年龄
        :param user_id:
        :return:
        """
        # update a single user

        params = utils.valid_params()
        if params is None:
            return utils.generate_ret(ErrorNo.INVALID_ARGUMENT)
        tmpUser = User.query.filter_by(id=user_id).first()
        age = params.get('age')
        if tmpUser:
            if age > 0:
                tmpUser.age = age
                db.session.add(tmpUser)
                db.session.commit()
                return utils.generate_ret(ErrorNo.SUCCESS)
            else:
                return utils.generate_ret(ErrorNo.INVALID_OPERATION)
        else:
            return utils.generate_ret(ErrorNo.OBJECT_NOT_EXIST)
