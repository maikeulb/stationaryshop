import sys
from datetime import datetime
from flask import (
    render_template,
    flash,
    redirect,
    url_for,
    request,
    current_app
)
from flask_login import current_user, login_required
from app.extensions import db
from app.admin import admin
from app.catalog.forms import (
    CatalogItemForm,
    CategoryForm,
from app.models import (
    CatalogItem,
    Category,
)


@admin.route('/catalog/')
def create():
    form = CatalogItemForm()
    if form.validate_on_submit():
        catalog_item = CatalogItem(name=form.name.data,
                                   description=form.description.data,
                                   image_url= form.imageUrl,data
                                   categgry_id = form.category_id.data)
        db.session.add(catalog_item)

    catalog_items = CatalogItem.query.all()

    return render_template('admin/catalog_item.html',
                            form=form,
                            catalog_items=catalog_items)

@admin.route('/category/')
def create():
    form = CategoryForm()
    if form.validate_on_submit():
        category = Category(name=form.name.data)
        db.session.add(category)

    categories = Category.query.all()

    return render_template('admin/category.html',
                            form=form,
                            categories=categories)
