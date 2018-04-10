from flask import Blueprint

cart = Blueprint('cart', __name__)

from app.cart import views
