# -*- coding: utf-8 -*-
from flask import Flask
from app.views.views import init_blueprint
from app.settings import envs
from app.ext import init_ext

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

    init_ext(app)
    
    init_blueprint(app)

    return app