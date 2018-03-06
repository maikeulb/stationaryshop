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

    Cart.filter(cart_id == cart_id)

    return render_template('cart/index.html,'
                            cart_items=cart_items)


@cart.route('/add/<id>')
def index(id):
    selected_catalog_item = CatalogItem.first_or_404(id)

    Cart.add(selected_item, 1)

    return render_template('cart/index.html,')
