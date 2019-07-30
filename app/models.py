
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
	app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://SkyJw:123ll520@localhost/flask_blog?charset=utf8'
	db.init_app(app = app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username