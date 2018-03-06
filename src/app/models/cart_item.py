from app.extensions import db
from datetime import datetime
from time import time
from flask import current_app
from app.search import add_to_index, remove_from_index, query_index
from app.models.message import Message


class Cart.Model:
    __tablename__ = 'cart_items'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer)
    catalog_item = db.Column(db.Integer)

    cart_item = db.relationship(
        'CartItem',
        backref='author',
    )
