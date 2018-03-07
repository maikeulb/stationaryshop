from app.extensions import db
from datetime import datetime
from time import time
from flask import current_app

class Cart(db.Model):
    __tablename__ = 'carts'

    id = db.Column(db.String, primary_key=True)

    cart_items = db.relationship(
        'CartItem'
    )
