from os import path

class Config(object):
    pass

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI='sqlite:///' + path.join(path.pardir,'database_test.db')
    Debug=True
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY='GunnsqkufcrsqwuLjCG'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    Debug=True
    SQLALCHEMY_DATABASE_URI='sqlite:///' + path.join(path.pardir,'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY='GunnsqkufcrsqwuLjCG'
