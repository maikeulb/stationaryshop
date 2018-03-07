from app.extensions import db
from datetime import datetime
from time import time
from flask import current_app
from app.models.order import Order
from app.models.catalog_item import CatalogItem


class OrderDetail(db.Model):
    __tablename__ = 'order_details'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer)
    price = db.Column(db.Numeric)

    catalog_item = db.relationship(
        'CatalogItem',
    )
