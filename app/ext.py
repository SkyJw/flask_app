from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate

db = SQLAlchemy()

def init_ext(app):
    db.init_app(app = app)
    Session(app)
    Bootstrap(app)
    migrate = Migrate(app, db)