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
from app.posts import posts
from app.posts.forms import (
    CommentForm,
    UploadForm
)
from app.models import (
    Post,
    Comment,
)


@cart.route('/index')
def index(category):

    if 'cart_id' in session:
       g.cart_id = session['cart_id']
    else:
       session['cart_id'] = random(int)

    ShoppingCart.filter(cart_id == cart_id)

    return render_template('cart/index.html,'
                            cart_items=cart_items)


@cart.route('/addToCart/<id>')
def index(id):
    selected_catalog_item = Catalog_item.first_or_404(id)

    Cart.Add(selected_item, 1)

    return render_template('cart/index.html,')
