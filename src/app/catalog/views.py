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
from app.catalog import catalog
from app.catalog.forms import SearchForm
from app.models import (
    Cart,
    Category,
    CartItem,
    CatalogItem,
)
import uuid
from sqlalchemy import func


@catalog.before_app_request
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
    g.search_form = SearchForm()


@catalog.route('/', defaults={'id': None})
@catalog.route('/<int:id>')
@catalog.route('/index/', defaults={'id': None})
@catalog.route('/index/<int:id>')
def index(id):
    if id is None:
        catalog_items_query = CatalogItem.query
        current_category = 'All Items'
    else:
        catalog_items_query = CatalogItem.query \
            .filter_by(category_id=id)
        current_category = Category.query \
            .filter_by(id=id) \
            .first_or_404().name

    if g.search_form.validate():
        q = g.search_form.q.data,

        catalog_items_query = \
            CatalogItem.query.filter(func.lower(CatalogItem.name).contains(func.lower(q)) |
                                     func.lower(CatalogItem.description).contains(func.lower(q)) |
                                     CatalogItem.category.has(name=(func.lower(q))))

    catalog_items = catalog_items_query.order_by(CatalogItem.name.desc())
    categories = Category.query.order_by(Category.name.desc())
    cart_items = g.cart.cart_items
    cart_quantity = sum([item.amount for item in cart_items])
    return render_template('catalog/index.html',
                           title="Catalog",
                           cart_quantity=cart_quantity,
                           catalog_items=catalog_items,
                           categories=categories,
                           current_category=current_category)
