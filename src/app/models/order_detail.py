from app.extensions import db
from datetime import datetime
from time import time
from flask import current_app
from app.search import add_to_index, remove_from_index, query_index
from app.models.message import Message


class OrderDetail.Model:
    __tablename__ = 'order_details'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer)
    price = db.Column(db.Integer)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))
    catalog_item_id = db.Column(db.Integer, db.ForeignKey('catalog_item.id'))

    cart_item = db.relationship(
        'CartItem',
    )

    order = db.relationship(
        'Order',
    )
