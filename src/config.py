import os
import redis


class Config(object):
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD') or 'P@ssw0rd!'
    ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL') or 'admin@email.com'

    DEMO_PASSWORD = os.environ.get('DEMO_PASSWORD') or 'P@ssw0rd!'
    DEMO_EMAIL = 'demo@email.com'

    DEMO_ADMIN_PASSWORD = os.environ.get('DEMO_ADMIN_PASSWORD') or 'P@ssw0rd!'
    DEMO_ADMIN_EMAIL = 'demo_admin@mail.com'

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'S3cr3t'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
        'postgresql://postgres:P@ssw0rd!@172.17.0.2/stationaryshop'

    REDIS_HOST = os.getenv('REDIS_HOST', '172.17.0.3')
    REDIS_PORT = os.getenv('REDIS_PORT', 6379)

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SESSION_TYPE = 'redis'

    LANGUAGES = ['en', 'ja']

    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')

    POSTS_PER_PAGE = 10

    DEBUG_TB_INTERCEPT_REDIRECTS = False
    DEVELOPMENT = False
    TESTING = False
    PRODUCTION = False
    DEBUG = False
    TESTING = False

    STRIPE_SECRET_KEY = os.environ.get('SECRET_KEY') or ''
    STRIPE_PUBLISHABLE_KEY = os.environ.get('PUBLISHABLE_KEY') or ''


class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True


class ProductionConfig(Config):
    PRODUCTION = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    CSRF_ENABLED = False
    WTF_CSRF_ENABLED = False
