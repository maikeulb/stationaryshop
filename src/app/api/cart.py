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


@api.route('/cart/<int:id>', methods=['POST'])
def add_to_cart(id):
    selected_catalog_item = CatalogItem.query \
        .filter_by(id=id) \
        .first()

    if selected_catalog_item is not None:

        cart_item = CartItem.query \
        .filter_by(catalog_item_id=id, cart_id=g.cart_id) \
        .first()

        if cart_item is None:
            cart_item = CartItem(cart_id=g.cart_id,
                                catalog_item=selected_catalog_item,
                                amount=1)
            db.session.add(cart_item)
        else:
            cart_item.amount += 1

        db.session.commit()
        return jsonify({'result': id})

    return jsonify({'result': 0})


@api.route('/cart/<int:id>', methods=['DELETE'])
def remove_from_cart(id):
    selected_catalog_item = CatalogItem.query \
        .filter_by(id=id) \
        .first()

    if selected_catalog_item is not None:

        cart_item = CartItem.query \
            .filter_by(catalog_item_id=id, cart_id=g.cart_id)\
            .first()

        if cart_item:
            if cart_item.amount > 1:
                cart_item.amount -= 1
            else:
                db.session.delete(cart_item)
            db.session.commit()
            return jsonify({'result': id})

        return jsonify({'result': 0})

    return jsonify({'result': 0})
