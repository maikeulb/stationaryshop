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
from app.extensions import db
from app.order import order
from app.order.forms import (
    OrderForm,
)
from app.models import (
    Cart,
    Order,
)


@order.route('/index')
def index():
    form = OrderForm()
    ##
    if 'cart_id' in session:
        g.cart_id = session['cart_id']
    else:
        session['cart_id'] = random(int)
    ##

    if form.validate_on_submit():
        cart = Cart.query \
            .filter_by(cart_id=cart_id) \
            .all()
        cart.cart_items = form.cart_items.data
        order = Order(order_lines=form.order_lines.data)
        cart.cart_items.remove(cart_items)
        db.session.commit()
        return redirect(url_for('order.complete'))
    return render_template('order/index.html',
                           form=form)


@order.route('/complete')
def index():
    return render_template('order/complete.html')
