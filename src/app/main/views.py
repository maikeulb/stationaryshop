import sys
from datetime import datetime
from flask import (
    render_template,
    flash,
    g,
    session,
    redirect,
    url_for,
    request,
    current_app
)
from flask_login import current_user, login_required
from app.extensions import db
from app.main import main
from app.models import (
    Cart,
    Category,
    CartItem,
    CatalogItem,
)
import uuid


@main.before_app_request
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


# @main.route('/', defaults={'category': None})
# @main.route('/index', defaults={'category': None})
# def index(category):
#     category = None
#     if category is None:
#         catalog_items = CatalogItem.query \
#             .all()
#         current_category = 'All Items'
#     else:
#         catalog_items = CatalogItem.query \
#             .filter_by(category=category) \
#             .all()
#         current_category = Category.query \
#             .filter_by(category=category) \
#             .first_or_default().name
#     categories = Category.query \
#         .order_by(Category.name.desc())

@main.route('/')
@main.route('/index')
def index():
    categories = Category.query \
        .order_by(Category.name.desc())
    cart_items = g.cart.cart_items
    cart_quantity = sum([item.amount for item in cart_items])

    return render_template('main/index.html',
                           categories=categories,
                           cart_quantity=cart_quantity)
