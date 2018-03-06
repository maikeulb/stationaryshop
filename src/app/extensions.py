from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

bcrypt = Bcrypt()
csrf_protect = CSRFProtect()
login = LoginManager()
login.login_view = 'account.login'
login.login_message = ('Please log in to access this page.')
db = SQLAlchemy()
migrate = Migrate()
