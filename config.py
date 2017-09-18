#-*- encoding:utf-8 -*-


class Config(object):
    """Base config class."""
    pass

class ProdConfig(Config):
    """Production config class."""
    pass

class DevConfig(Config):
    """Development config class."""
    # Open the DEBUG
    DEBUG = True
    # MySQL connection
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:tApn8wVauUzQe0En@192.168.121.23:3306/flaskblog'
