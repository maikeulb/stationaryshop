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
from app.extensions import db, stripe_keys
from app.cart import cart
from app.models import (
    Cart,
    Category,
    CartItem,
    CatalogItem,
)
import json
import uuid
import stripe


@cart.before_app_request
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


@cart.route('/')
@cart.route('/index')
def index():

    cart_items = CartItem.query \
        .filter_by(cart_id=g.cart_id) \
        .all()

    g.cart.cart_items = cart_items

    cart_item_prices = [
        cart_item.catalog_item.price for cart_item in cart_items]
    cart_item_amounts = [cart_item.amount for cart_item in cart_items]

    cart_total = sum((a * p for a, p in zip(cart_item_prices,
                                            cart_item_amounts)))

    print(cart_total, sys.stdout)

    db.session.add(g.cart)
    db.session.commit()

    categories = Category.query \
        .order_by(Category.name.desc())
    cart_items = g.cart.cart_items,

    return render_template('cart/index.html',
                           cart_items=cart_items,
                           cart=g.cart,
                           categories=categories,
                           cart_total=cart_total,
                           key=stripe_keys['publishable_key'])


@cart.route('/add/<int:catalog_item_id>')
def add_to_cart(catalog_item_id):
    selected_catalog_item = CatalogItem.query \
        .filter_by(id=catalog_item_id) \
        .first_or_404()

    if selected_catalog_item is not None:

        cart_item = CartItem.query \
            .filter_by(catalog_item_id=catalog_item_id, cart_id=g.cart_id) \
            .first()

        if cart_item is None:
            cart_item = CartItem(cart_id=g.cart_id,
                                 catalog_item=selected_catalog_item,
                                 amount=1)
            db.session.add(cart_item)
        else:
            cart_item.amount += 1

        db.session.commit()

    return redirect(url_for('cart.index'))


@cart.route('/remove/<int:catalog_item_id>')
def remove_from_cart(catalog_item_id):
    selected_catalog_item = CatalogItem.query \
        .filter_by(id=catalog_item_id) \
        .first_or_404()

    if selected_catalog_item is not None:

        cart_item = CartItem.query \
            .filter_by(catalog_item_id=catalog_item_id, cart_id=g.cart_id)\
            .first_or_404()

        if cart_item:
            if cart_item.amount > 1:
                cart_item.amount -= 1
            else:
                db.session.delete(cart_item)

        db.session.commit()

    return redirect(url_for('cart.index'))
