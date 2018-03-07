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
from app.catalog import catalog
from app.models import (
    CatalogItem,
    Category,
)


@catalog.route('/', defaults={'id': None})
@catalog.route('/<int:id>')
@catalog.route('/index/', defaults={'id': None})
@catalog.route('/index/<int:id>')
def index(id):
    if id is None:
        catalog_items = CatalogItem.query \
            .all()
        current_category = 'All Items'
    else:
        catalog_items = CatalogItem.query \
                .filter_by(category_id=id) \
                .all()
        current_category = Category.query \
                .filter_by(id=id) \
                .first_or_404().name
    categories = Category.query \
        .order_by(Category.name.desc())
    return render_template('catalog/index.html',
                            catalog_items=catalog_items,
                            categories=categories,
                            current_category=current_category)


@catalog.route('/details/<id>')
def details(id):
    catalog_item = CatalogItem.query \
        .filter_by(id=id) \
        .first_or_404()
    categories = Category.query \
        .order_by(Category.name.desc())
    return render_template('catalog/details.html',
                            categories=categories,
                            catalog_item=catalog_item)
