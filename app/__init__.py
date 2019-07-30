# -*- coding: utf-8 -*-
#初始化flask app，注册蓝图
from flask import Flask, session
from flask_session import Session

from flask_bootstrap import Bootstrap

from app.models import init_db
from app.views.views import init_blueprint
from app.setting import envs

def create_app():
    #使用static_folder参数指定static文件路径，html中去获取static文件时，默认的起点路径变成此处指定的路径
    app = Flask(__name__, static_folder = '../static')

    #app配置
    #app.config["SECRET_KEY"] = 'fjw123520999'
    #app.config['SESSION_TYPE'] = 'redis'
    #app.config['SESSION_REDIS'] = StrictRedis(host='localhost', port=6379)    
    #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #采用单独文件存储配置对象，对app进行配置
    app.config.from_object(envs.get('develop'))

    Session(app)
    Bootstrap(app)

    
    init_db(app)
    
    init_blueprint(app)

    return app