from datetime import timedelta


ACCESS_TOKEN_EXPIRE_TIME = timedelta(minutes=30)
REFRESH_TOKEN_EXPIRE_TIME = timedelta(weeks=2)


class BaseAppConfig:
    SECRET_KEY = 'super-extreme-hard-key'
    JWT_ACCESS_TOKEN_EXPIRES = ACCESS_TOKEN_EXPIRE_TIME
    JWT_REFRESH_TOKEN_EXPIRES = REFRESH_TOKEN_EXPIRE_TIME


class LocalAppConfig:
    RUN_SETTINGS = {
        'host': '127.0.0.1',
        'port': 5000,
        'debug': True
    }


class AWSAppConfig:
    RUN_SETTINGS = {
        'host': '0.0.0.0',
        'port': 80,
        'debug': False
    }