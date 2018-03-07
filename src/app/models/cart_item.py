from app.extensions import db
from datetime import datetime
from time import time
from flask import current_app
from app.models.catalog_item import CatalogItem


class CartItem(db.Model):
    __tablename__ = 'cart_items'

    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer)
    cart_id = db.Column(db.String, db.ForeignKey('carts.id'))

    catalog_item = db.relationship(
        'CatalogItem'
    )
