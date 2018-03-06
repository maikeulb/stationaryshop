from app.extensions import db
from datetime import datetime
from time import time
from flask import current_app
from app.search import add_to_index, remove_from_index, query_index
from app.models.message import Message


class Cart.Model:
    __tablename__ = 'carts'

    id = db.Column(db.Integer, primary_key=True)

    cart_items = db.relationship(
        'CartItem'
    )
