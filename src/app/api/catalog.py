import sys
from datetime import datetime
from flask import (
    render_template,
    flash,
    redirect,
    url_for,
    request,
    jsonify,
    current_app
)
from flask_login import current_user, login_required
from app.extensions import db
from app.api import api
from app.models import (
    Cart,
    CartItem,
    Catalog,
)
import json


@api.route('/catalog/', methods=['post'])
def add_to_cart():
    catalog_items = CatalogItem.query \
        .order_by()

    return jsonify(catalog_items)

