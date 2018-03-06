from app.extensions import db
from datetime import datetime
from time import time
from flask import current_app
from app.search import add_to_index, remove_from_index, query_index
from app.models.message import Message


class CatalogItem.Model:
    __tablename__ = 'CatalogItem'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer)
    description = db.Column(db.String(140))
    imageUrl = db.Column(db.String(140))
    category_Id  = db.Column(db.Integer, db.ForeignKey('categories.id'))

    cart_item = db.relationship(
        'CartItem',
    )

    category = db.relationship(
        'Category',
    )
