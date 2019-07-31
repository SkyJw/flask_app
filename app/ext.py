from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_bootstrap import Bootstrap

db = SQLAlchemy()

def init_ext(app):
    db.init_app(app = app)
    Session(app)
    Bootstrap(app)