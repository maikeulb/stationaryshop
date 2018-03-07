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
from app.main import main
from app.models import (
    CatalogItem,
    Category,
)


@main.route('/', defaults={'category': None})
@main.route('/index', defaults={'category': None})
def index(category):
    category = None
    if category is None:
        catalog_items = CatalogItem.query \
            .all()
        current_category = 'All Items'
    else:
        catalog_items = CatalogItem.query \
                .filter_by(category=category) \
                .all()
        current_category = Category.query \
                .filter_by(category=category) \
                .first_or_default().name

    return render_template('main/index.html',
                            catalog_items=catalog_items,
                            current_category=current_category)
