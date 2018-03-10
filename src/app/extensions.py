from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from simplekv.memory.redisstore import RedisStore
import redis
import os

bcrypt = Bcrypt()
csrf_protect = CSRFProtect()
login = LoginManager()
login.login_view = 'account.login'
login.login_message = ('Please log in to access this page.')
db = SQLAlchemy()
migrate = Migrate()
store = RedisStore(redis.StrictRedis())
stripe_keys = {
    'secret_key': os.environ['SECRET_KEY'],
    'publishable_key': os.environ['PUBLISHABLE_KEY']
}
