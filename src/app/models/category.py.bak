from app.extensions import db
from datetime import datetime
from time import time
from flask import current_app


class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    catalog_items = db.relationship(
        'CatalogItem',
        backref='category'
    )
