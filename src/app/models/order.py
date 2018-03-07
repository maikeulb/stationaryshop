from app.extensions import db
from datetime import datetime
from time import time
from flask import current_app


class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    order_total = db.Column(db.Numeric)
    order_placed = db.Column(db.DateTime, default = datetime.utcnow)
    order_detail_id = db.Column(db.Integer, db.ForeignKey('order_details.id'))

    order_lines = db.relationship(
        'OrderDetail',
    )
