from flask import Blueprint

catalog = Blueprint('catalog', __name__)

from app.catalog import views
