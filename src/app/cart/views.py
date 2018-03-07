import sys
from datetime import datetime
from sqlalchemy import and_
from flask import (
    render_template,
    flash,
    redirect,
    url_for,
    request,
    current_app
)
from flask_login import current_user, login_required
from app.extensions import db
from app.cart import cart
from app.models import (
    Cart,
    Category,
    CatalogItem,
)


@cart.route('/index')
def index():

    ## movies to before_request
    if 'cart_id' in session:
       g.cart_id = session['cart_id']
    else:
       session['cart_id'] = uuid.uuid4()
    ####

    cart_items_from_session = Cart.query \
        .filter_by(cart_id=cart_id) \
        .all()

    cart = Cart(cart_items=cart_items)

    zipped_cart_items = zip(cart_items.price, cart_items.amount)
    cart_total = [sum(cart_item) for cart_item in zipped_cart_items]

    db.session.add(cart)
    db.session.commit()

    return render_template('cart/index.html',
                            cart=cart,
                            cart_total=cart_total)


@cart.route('/add/')
def add_to_cart():
    data = request.data
    dataDict = json.loads(data)

    ## movies to before_request
    if 'cart_id' in session:
        g.cart_id = session['cart_id']
    else:
        session['cart_id'] = random(int)
    ####

    selected_catalog_item = Cart.query \
        .filter_by(catalog_it=dataDict['catalog_id'], cart_id=cart_id)\
        .single_or_404()

    if cart_item is null:
        cart = Cart(cart_id = cart_id,
                     catalog_item=selected_catalog_item,
                     amount=1)
        db.session.add(cart)
    else:
        cart.cart_item.amount += 1
    db.session.commit()

    return redirect(url_for('cart.index'))

@cart.route('/remove/')
def remove_from_cart(id):
    data = request.data
    dataDict = json.loads(data)

    ####
    if 'cart_id' in session:
        g.cart_id = session['cart_id']
    else:
        session['cart_id'] = random(int)
    ####

    cart_item = CartItem.query \
        .filter_by(catalog_it=dataDict['catalog_id'], cart_id=cart_id) \
        .single_or_404()

    if cart_item:
        if cart_item.amount > 1:
            cart_item.amount -=1
        else:
            db.session.delete(cart_item)
            db.session.commit()

    return redirect(url_for('cart.index'))
