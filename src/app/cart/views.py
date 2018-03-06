import sys
from datetime import datetime
from flask import (
    render_template,
    flash,
    redirect,
    url_for,
    request,
    current_app
)
from flask_login import current_user, login_required
from app.extensions import db, images
from app.cart import cart
from app.cart.forms import (
    CartForm,
)
from app.models import (
    Cart,
    Category,
    CatalogItem,
)


@cart.route('/index')
def index(category):

    if 'cart_id' in session:
       g.cart_id = session['cart_id']
    else:
       session['cart_id'] = random(int)

    cart_items_from_session = Cart.query
        .filter_by(cart_id == cart_id)
        .all()

    cart = Cart(cart_items=cart_items)
    cart_total = Cart.where(cart_id == cart_id)
        .func.sum(catalog_item.price * catalog_item.amount)
    db.session.add(cart_items)
    db.session.commit()
    return render_template('cart/index.html,'
                            cart=cart,
                            cart_total=cart_total)


@cart.route('/add/<id>')
def add_to_cart(id):
    data = request.data
    dataDict = json.loads(data)

    if 'cart_id' in session:
        g.cart_id = session['cart_id']
    else:
        session['cart_id'] = random(int)

    selected_catalog_item = CartItem.query \
        .filter_by(dataDict['id'] and cart_id) \
        .single_or_404()

    if selected_catalog_item != null:
        if cart_item==null:
            cart_item = Cart(cart_id = cart_id,
                        catalog_item=selected_catalog_item,
                         amount=1)
            db.session.add(cart_item)
        else:
            cart_item.amount += 1
        db.session.commit()

    return redirect(url_for('cart.index'))

@cart.route('/remove/')
def remove_from_cart(id):
    data = request.data
    dataDict = json.loads(data)

    if 'cart_id' in session:
        g.cart_id = session['cart_id']
    else:
        session['cart_id'] = random(int)

    catalog_item = CartItem.query \
        .filter_by(dataDict['id'] and cart_id) \
        .first_or_404()

    if catalog_item.amount is 1:
        db.session.remove(cart_item)
    else:
        cart_item.amount -= 1
    db.session.commit()

    return redirect(url_for('cart.index'))
