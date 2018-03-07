from app.extensions import db
from datetime import datetime
from time import time
from flask import current_app
from app.models.category import Category


class CatalogItem(db.Model):
    __tablename__ = 'catalog_items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer)
    description = db.Column(db.String(140))
    imageUrl = db.Column(db.String(140))
    price  = db.Column(db.Numeric)
    is_sale_item  = db.Column(db.Boolean)
    cart_item_id = db.Column(db.Integer,db.ForeignKey('cart_items.id'))
    order_detail_id = db.Column(db.Integer,db.ForeignKey('order_details.id'))
    categories_id = db.Column(db.Integer,db.ForeignKey('categories.id'))
