from flask import Blueprint

order = Blueprint('order', __name__)

from app.order import views
