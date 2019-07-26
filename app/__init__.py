#初始化flask app，注册蓝图

from flask import Flask

from app.views.views import blog_bp

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "123520999"

	#url_prefix：添加url链接前缀
    #app.register_blueprint(blueprint=blog_bp, url_prefix = '/blog')
    app.register_blueprint(blueprint=blog_bp) 

    return app