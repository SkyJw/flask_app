# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, request, Response, make_response, redirect, url_for, session

#url和xxx.html没有绝对的对应关系

#蓝图模版路径的起点是创建蓝图的文件的所在路径
#想指定静态文件路径时，发现在蓝图处使用static_folder参数指定不好使，需要在创建Flask时指定
blog_bp = Blueprint('blog', __name__, template_folder = '../../templates')


@blog_bp.route('/')
def test():
	return 'Hello'

@blog_bp.route('/index/')
def index():
	#cookies方式跨页面获取数据，获取请求中的cookies数据
	#username = request.cookies.get('username', '游客')

	#session方式跨页面
	username = session.get('username','游客')

	return render_template('index.html', username = username)

@blog_bp.route('/login/')
def user_login():
	return render_template('UserLogin.html')

@blog_bp.route('/logout/')
def user_logout():
	return render_template('__base__.html')

@blog_bp.route('/douserlogin', methods = ['POST', 'GET'])
def do_user_login():
	name = request.form.get('username')

	print(name)

	resp = redirect(url_for('blog.index'))

	#cookies方式跨页面获取数据，首先在服务器端设置cookie
	#resp.set_cookie('username', name)

	#session方式跨页面
	session['username'] = name

	return resp

@blog_bp.route('/hellobootstrap')
def hello_bs():
	return render_template('hello_bootstrap.html')