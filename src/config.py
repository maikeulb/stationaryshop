import os
import redis
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(dotenv_path)


class Config(object):

    ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD')
    ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL')

    DEMO_PASSWORD = os.environ.get('DEMO_PASSWORD') or 'P@ssw0rd!'
    DEMO_EMAIL = 'demo@email.com'

    DEMO_ADMIN_PASSWORD = os.environ.get('DEMO_ADMIN_PASSWORD') or 'P@ssw0rd!'
    DEMO_ADMIN_EMAIL = 'demo_admin@mail.com'

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'S3cr3t'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or \
        'postgresql://postgres:P@ssw0rd!@172.17.0.2/stationaryshop'
    ELASTICSEARCH_URL = os.environ.get('ELASTIC_URI') or \
        'http://172.17.0.5:9200'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_TYPE = 'redis'
    SESSION_REDIS = redis.from_url('localhost:6379')

    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')

    POSTS_PER_PAGE = 10

    DEBUG_TB_INTERCEPT_REDIRECTS = False
    DEVELOPMENT = False
    TESTING = False
    PRODUCTION = False
    DEBUG = False
    TESTING = False

    SECRET_KEY = os.environ.get('SECRET_KEY')
    PUBLISHABLE_KEY = os.environ.get('PUBLISHABLE_KEY')


class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
    DEBUG_TB_ENABLED = True
    # CACHE_TYPE = 'simple'


class ProductionConfig(Config):
    DATABASE_URI = ''
    PRODUCTION = True


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    CSRF_ENABLED = False
    WTF_CSRF_ENABLED = False
