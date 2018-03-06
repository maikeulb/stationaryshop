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
from app.order import order
from app.order.forms import (
    OrderForm,
)
from app.models import (
    Cart,
    Order,
)


@order.route('/index')
def index(order):

    if 'cart_id' in session:
        g.cart_id = session['cart_id']
    else:
        session['cart_id'] = random(int)

    if form.validate_on_submit():
        cart_items = Cart \
            .filter_by(cart_id == cart_id) \
            .all()
        Cartcart_items = form.cart_items.data
        Order.create_order()
        Cart.clear_cart()
    return redirect(url_for('order.complete'))


@order.route('/complete')
def index():
    return render_template('order/complete.html')
