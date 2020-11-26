import os
FLASK = os.environ


class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite:///:memory:'


class ProductionConfig(Config):
    SECRET_KEY = 'prd'
    DATABASE_URI = 'mysql://user@localhost/foo'


class DevelopmentConfig(Config):
    DEBUG = FLASK.get('DEBUG')
    SECRET_KEY = FLASK.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.path.join(FLASK.get('SQLALCHEMY_DATABASE_URI'))
    SQLALCHEMY_TRACK_MODIFICATIONS = FLASK.get('SQLALCHEMY_TRACK_MODIFICATIONS')
    SQLALCHEMY_ECHO = True


class TestingConfig(Config):
    SECRET_KEY = 'test'
    TESTING = True


def loadConfig(env):
    configs = {
        'development': DevelopmentConfig,
        'production': ProductionConfig,
        'test': TestingConfig
    }
    return configs.get(env)
