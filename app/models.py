# -*- coding:utf-8 -*-

from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from . import utils
import pymysql


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:123456@localhost/flask_app"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)


# 会员数据模型
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), unique=True)
    pwd = db.Column(db.String(100))
    email = db.Column(db.String(100))
    age = db.Column(db.String(10), default='18')
    phone = db.Column(db.String(11), unique=True)
    info = db.Column(db.Text)
    face = db.Column(db.String(255))
    sex = db.Column(db.Integer, default=0)
    status = db.Column(db.Integer, default=0)
    addtime = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    # posts = db.relationship('Posts', backref="user", cascade="all, delete,delete-orphan")
    # comments = db.relationship('Comments', backref="user", cascade="all, delete,delete-orphan")
    # reply = db.relationship('Reply', backref="user", cascade="all, delete,delete-orphan")

    # 加密
    @classmethod
    def MD5password(cls, password):
        import hashlib
        # 创建md5对象
        hl = hashlib.md5()
        hl.update(password.encode(encoding='utf-8'))
        return hl.hexdigest()

    def __repr__(self):
        return self.name

    def to_dict(self):
        """
        将对象转换为字典数据
        """
        user_dict = {
            "id": self.id,
            "name": self.name,
            "pwd": self.pwd,
            "email": self.email,
            "age": self.age,
            "phone": self.phone,
            "info": self.info,
            "face": self.face,
            "sex": self.sex,
            "status": self.status,
            "addtime": utils.datetime2str(self.addtime)
        }
        return user_dict


manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
