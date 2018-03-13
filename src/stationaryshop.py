import os
from app import create_app, cli
from app.extensions import db
from app.models import User, Cart

app = create_app(os.getenv('FLASK_APP_CONFIG') or 'config.DevelopmentConfig')
cli.register(app)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Cart': Cart}
