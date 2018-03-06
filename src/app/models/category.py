from app.extensions import db
from datetime import datetime
from time import time
from flask import current_app
from app.search import add_to_index, remove_from_index, query_index
from app.models.message import Message


class Category.Model:
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer)
    description = db.Column(db.Integer)

    cart_items = db.relationship(
        'CartItem',
    )
