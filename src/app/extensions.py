import os

from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_mail import Mail
from flask_session import Session
from simplekv.memory.redisstore import RedisStore
from config import Config
from redis import StrictRedis
from sqlalchemy_searchable import SearchQueryMixin
import stripe

bcrypt = Bcrypt()
csrf_protect = CSRFProtect()
login = LoginManager()
login.login_view = 'account.login'
login.login_message = ('Please log in to access this page.')
db = SQLAlchemy()
migrate = Migrate()
store = RedisStore(StrictRedis(host=Config.REDIS_HOST,
                               port=Config.REDIS_PORT,
                               db=0))
stripe_keys = {
    'secret_key': os.environ['STRIPE_SECRET_KEY'] or '',
    'publishable_key': os.environ['STRIPE_PUBLISHABLE_KEY'] or ''
}
stripe.api_key = stripe_keys['secret_key']
mail = Mail()
