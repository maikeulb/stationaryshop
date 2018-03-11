from app.extensions import db
from datetime import datetime
from time import time
from flask import current_app
from app.models.category import Category


class CatalogItem(db.Model):
    __tablename__ = 'catalog_items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(140))
    image_url = db.Column(db.String(140))
    price = db.Column(db.Numeric)
    order_detail_id = db.Column(db.Integer, db.ForeignKey('order_details.id'))
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))

    def from_dict(self, data):
        for field in ['name', 'description', 'image_url',
                      'category_id', 'price']:
            if field in data:
                setattr(self, field, data[field])

    def to_dict(self):
        data = {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'image_url': self.image_url,
            'category_id': self.category_id,
            'price': str(self.price),
        }
        return data
