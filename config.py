import os
from typing import Type


class Config(object):
    DB_USER = os.getenv('DB_USER')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_NAME = os.getenv('DB_NAME')
    DB_HOST = os.getenv('DB_HOST')
    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_ECHO = False

class ConfigFactory:
    flask_env = os.getenv('FLASK_ENV')

    @classmethod
    def get_config(cls) -> Type[Config]:
        if cls.flask_env == 'development':
            return DevelopmentConfig
        elif cls.flask_env == 'production':
            return ProductionConfig
        raise NotImplementedError


config = ConfigFactory.get_config()