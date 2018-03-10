import sys
from datetime import datetime
from flask import (
    render_template,
    flash,
    g,
    jsonify,
    session,
    redirect,
    url_for,
    request,
    current_app
)
from flask_login import current_user, login_required
from app.extensions import db
from app.api import api
from app.models import (
    Cart,
    Category,
    CartItem,
    CatalogItem,
)
import json
import uuid


@api.before_app_request
def before_request():
    if 'cart_id' in session:
        g.cart_id = session['cart_id']
    else:
        g.cart_id = str(uuid.uuid4())
        session['cart_id'] = g.cart_id
    g.cart = Cart.query \
        .filter_by(id=g.cart_id) \
        .first()
    if g.cart is None:
        g.cart = Cart(id=g.cart_id)
        db.session.add(g.cart)


@api.route('/cartcomponent/')
def get_cart_quantity():
    cart_items = g.cart.cart_items
    cart_quantity = sum([item.amount for item in cart_items])
    return jsonify({'quantity': cart_quantity })
