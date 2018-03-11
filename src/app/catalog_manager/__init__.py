from flask import Blueprint

catalog_manager = Blueprint('catalog_manager', __name__)

from app.catalog_manager import views
