from app.extensions import db
from datetime import datetime
from time import time
from flask import current_app
from app.search import add_to_index, remove_from_index, query_index
from app.models.message import Message


class Order.Model:
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    order_total = db.Column(db.Integer)
    order_placed = db.Column(db.Integer)

    order_lines = db.relationship(
        'OrderDetail',
    )
