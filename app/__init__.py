# -*- coding: utf-8 -*-
#初始化flask app，注册蓝图
from flask import Flask, session
from flask_session import Session
from redis import StrictRedis
from flask_bootstrap import Bootstrap

from app.views.views import blog_bp

def create_app():
    #使用static_folder参数指定static文件路径，html中去获取static文件时，默认的起点路径变成此处指定的路径
    app = Flask(__name__, static_folder = '../static')

    app.config["SECRET_KEY"] = 'fjw123520999'
    app.config['SESSION_TYPE'] = 'redis'
    app.config['SESSION_REDIS'] = StrictRedis(host='localhost', port=6379)    
    #app.config['SESSION_REDIS'] = StrictRedis(host='localhost', port=6379,decode_responses=True)

    Session(app)
    Bootstrap(app)
    
	#url_prefix：添加url链接前缀
    #app.register_blueprint(blueprint=blog_bp, url_prefix = '/blog')
    app.register_blueprint(blueprint=blog_bp) 

    return app