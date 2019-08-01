from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def init_ext(app):
    db.init_app(app = app)
    migrate.init_app(app = app, db = db)
    Session(app)
    Bootstrap(app)