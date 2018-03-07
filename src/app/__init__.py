import config
import os
from flask_kvsession import KVSessionExtension

from flask import(
    Flask,
    render_template,
    request,
    current_app)
from app import commands
from app.account import account as account_bp
from app.extensions import(
    bcrypt,
    csrf_protect,
    db,
    login,
    store,
    migrate)
from app.main import main as main_bp
from app.cart import cart as cart_bp
from app.catalog import catalog as catalog_bp
from app.order import order as order_bp
from app.admin import admin as admin_bp
Config = eval(os.environ['FLASK_APP_CONFIG'])

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    register_commands(app)
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
    return None


def register_blueprints(app):
    app.register_blueprint(main_bp)
    app.register_blueprint(account_bp, url_prefix='/account')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(cart_bp, url_prefix='/cart')
    app.register_blueprint(catalog_bp, url_prefix='/catalog')
    app.register_blueprint(order_bp, url_prefix='/order')
    return None

def register_errorhandlers(app):
    def render_error(error):
        error_code = getattr(error, 'code', 500)
        return render_template('errors/{0}.html'.format(error_code)), error_code
    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)
    return None

def register_commands(app):
    app.cli.add_command(commands.test)
    app.cli.add_command(commands.lint)
    app.cli.add_command(commands.clean)
    app.cli.add_command(commands.urls)
    app.cli.add_command(commands.seed)
