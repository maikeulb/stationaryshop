from app.extensions import db
from datetime import datetime
from time import time
from flask import current_app
from app.search import add_to_index, remove_from_index, query_index
from app.models.message import Message


class CartItem.Model:
    __tablename__ = 'cart_items'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer)
    cart_id = db.Column(db.String, db.ForeignKey('carts.id'))

    catalog_item = db.relationship(
        'CatalogItem'
    )
