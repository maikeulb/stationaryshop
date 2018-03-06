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


@order.route('/index')
def index(order):
    if form.validate_on_submit():
        cart_items = ShoppingCart.get_cart_items()
        cart_items = form.cart_items.data
        Order.create_order()
        ShoppingCart.ClearCart()
    return redirect(url_for('order.complete'))


@order.route('/complete')
def index():
    return render_template('order/complete.html')
