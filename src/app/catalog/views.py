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


# @catalog.route('/index/<category>', defaults={'category': None})
# def index(category):
#     if category is None:
#         catalog_items=CatalogItem.query \
#             .order_by(id)
#         current_category = 'All Items';
#     else:
#         catalog_items = CatalogItem.query \
#                 .filter_by(category=category) \
#                 .order_by(category)
#         current_category = Category.query \
#                 .filter_by(category=category) \
#                 .first_or_default().name

    # return render_template('catalog/index.html',
    #                         catalog_items=catalog_items,
    #                         current_category=current_category)


@catalog.route('/details/<id>')
def details(id):
    catalog_item = CatalogItem.query \
        .filter_by(id=id) \
        .first_or_404()
    return render_template('catalog/details.html',
                            catalog_item=catalog_item)
