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


@catalog.route('/index')
def index(category):
    if category:
        catalog_items=CatalogItem.query.order_by(id)
        current_category = 'All Pies';
    catalog_items = CatalogItem \
            .filter(category=category) \
            .order_by(id);
    current_category = Category \
            .filter(category=category) \
            .categoryname \
            .first_or_default();
    return render_template('catalog/index.html,'
                            catalog_items=catalog_items,
                            current_category=current_category)


@catalog.route('/details/<id>')
def index(id):
    catalog_item = CatalogItem.get_by_id(id) \
    return render_template('catalog/details.html,'
                            catalog_item=catalog_item)
