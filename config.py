import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    SECRET_KEY = os.environ['SECRET_KEY']
    DB_USERNAME = os.environ['MYSQL_USER']
    DB_PASSWORD = os.environ['MYSQL_PASSWORD']
    DB_HOST = os.environ['MYSQL_HOST']
    DATABASE_NAME = os.environ['MYSQL_DATABASE']
    DB_URI = 'mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user=DB_USERNAME, password=DB_PASSWORD, server=DB_HOST, database=DATABASE_NAME)

    SQLALCHEMY_DATABASE_URI = DB_URI


class ProdConfig(Config):
    DEBUG = False


class TestConfig(Config):
    DEBUG = True


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True