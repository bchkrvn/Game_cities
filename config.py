import os
from typing import Type


class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


class ConfigFactory:
    flask_env = os.getenv('FLASK_ENV', 'development')
    print(flask_env)

    @classmethod
    def get_config(cls) -> Type[Config]:
        if cls.flask_env == 'development':
            return DevelopmentConfig
        elif cls.flask_env == 'production':
            return ProductionConfig
        raise NotImplementedError


config = ConfigFactory.get_config()