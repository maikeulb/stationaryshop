import sys
from datetime import datetime
from sqlalchemy import func
from flask import (
    render_template,
    flash,
    g,
    jsonify,
    session,
    redirect,
    url_for,
    request,
    current_app
)
from flask_login import current_user, login_required
from app.extensions import db
from app.api import api
from app.models import (
    Cart,
    Category,
    CartItem,
    CatalogItem,
)
import json
import uuid


@api.route('/catalogitems', defaults={'query': None})
def get_catalog_items(query):
    query = request.args.get('query')
    catalog_item_query = CatalogItem.query

    if query:
        catalog_item_query = \
            catalog_item_query.filter(func.lower(CatalogItem.first_name).contains(func.lower(query)) |
                                      func.lower(CatalogItem.last_name).contains(func.lower(query)))

    catalog_items = catalog_item_query.all()
    response = jsonify([catalog_item.to_dict() for catalog_item in
                        catalog_items])
    return response


@api.route('/catalogitems/<int:id>')
def get_catalogitems(id):
    catalog_item = CatalogItem.query.get_or_404(id)

    response = jsonify(catalog_item.to_dict())
    return response


@api.route('/catalogitems/<int:id>')
def get_catalogitem(id):
    catalog_item = CatalogItem.query.get_or_404(id)


@api.route('/catalogitems/', methods=['POST'])
def create_catalog_item():
    data = request.get_json() or {}

    catalog_item = CatalogItem()
    catalog_item.from_dict(data)

    db.session.add(catalog_item)
    db.session.commit()

    response = jsonify(catalog_item.to_dict())
    return response


@api.route('/catalogitems/<int:id>', methods=['PUT'])
def update_catalog_item(id):
    catalog_item = CatalogItem.query.filter_by(id=id).first_or_404()
    catalog_item.from_dict(request.get_json() or {})

    db.session.commit()

    response = jsonify(catalog_item.to_dict())
    return response


@api.route('/catalogitems/<int:id>', methods=['DELETE'])
def delete_catalog_item(id):
    CatalogItem.query.filter_by(id=id).delete()
    db.session.commit()

    response = jsonify({'data': 'success'})
    return response
