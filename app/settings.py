from redis import StrictRedis

def get_db_url(dbinfo):
    ENGINE = dbinfo.get('ENGINE') or 'mysql'

    DRIVER = dbinfo.get('DRIVER') or 'pymysql' 

    USER = dbinfo.get('USER') or 'root'

    PASSWORD = dbinfo.get('PASSWORD') or '123ll520'

    HOST = dbinfo.get('HOST') or 'localhost'

    PORT = dbinfo.get('PORT') or '3306'

    NAME = dbinfo.get('NAME') or 'flask_blog'

    return '{}+{}://{}:{}@{}:{}/{}'.format(ENGINE, DRIVER, USER, PASSWORD, HOST, PORT, NAME)


class Config:
    DEBUG = False

    TESTING = False

    SECRET_KEY = '12314CVSDFSDF'

    SESSION_TYPE = 'redis'

    SESSION_REDIS = StrictRedis(host='localhost', port=6379)

    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopConfig(Config):
    DEBUG = True

    DATABASE = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'SkyJw',
        'PASSWORD': '123ll520',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'flask_blog'
    }

    SQLALCHEMY_DATABASE_URI = get_db_url(DATABASE)

class TestingConfig(Config):
    TESTING = True

    DATABASE = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': '123ll520',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'flask_blog'
    }

    SQLALCHEMY_DATABASE_URL = get_db_url(DATABASE)

class StagingConfig(Config):

    DATABASE = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': '123ll520',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'flask_blog'
    }

    SQLALCHEMY_DATABASE_URL = get_db_url(DATABASE)

class ProductConfig(Config):

    DATABASE = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': '123ll520',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'flask_blog'
    }

    SQLALCHEMY_DATABASE_URL = get_db_url(DATABASE)

envs = {
    'develop': DevelopConfig,
    'testing': TestingConfig,
    'staging': StagingConfig,
    'product': ProductConfig
}