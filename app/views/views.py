from flask import Blueprint, render_template, request, Response, make_response, redirect, url_for, session

#url和xxx.html没有绝对的对应关系

#蓝图模版路径的起点是创建蓝图的文件的所在路径
blog_bp = Blueprint('blog', __name__, template_folder = '../../templates')

@blog_bp.route('/')
def test():
	return 'Hello'

@blog_bp.route('/index/')
def index():
	username = request.cookies.get('username', '游客')

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

	resp.set_cookie('username', name)


	return resp
