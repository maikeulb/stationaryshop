import config
import os
from flask_kvsession import KVSessionExtension
from logging.handlers import RotatingFileHandler
from flask import(
    Flask,
    render_template,
    request,
    current_app)
from app.account import account as account_bp
from app.extensions import(
    bcrypt,
    csrf_protect,
    db,
    login,
    store,
    migrate)
from app.api import api as api_bp
from app.main import main as main_bp
from app.cart import cart as cart_bp
from app.catalog import catalog as catalog_bp
from app.order import order as order_bp
from app.catalog_manager import catalog_manager as catalog_manager_bp
import stripe
from flask_babel import Babel, lazy_gettext as _l
Config = eval(os.environ['FLASK_APP_CONFIG'])


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    register_blueprints(app)
    register_extensions(app)
    register_errorhandlers(app)
    return app


def register_extensions(app):
    bcrypt.init_app(app)
    db.init_app(app)
    csrf_protect.init_app(app)
    login.init_app(app)
    migrate.init_app(app, db)
    KVSessionExtension(store, app)
    babel = Babel(app)

    @babel.localeselector
    def get_locale():
        # return 'ja'
        return request.accept_languages \
            .best_match(current_app.config['LANGUAGES'])
    return None


def register_blueprints(app):
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(account_bp, url_prefix='/account')
    app.register_blueprint(cart_bp, url_prefix='/cart')
    app.register_blueprint(catalog_bp, url_prefix='/catalog')
    app.register_blueprint(order_bp, url_prefix='/order')
    app.register_blueprint(catalog_manager_bp, url_prefix='/catalogmanager')
    return None


def register_errorhandlers(app):
    def render_error(error):
        error_code = getattr(error, 'code', 500)
        return render_template('errors/{0}.html'.format(error_code)), error_code
    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)
    return None
