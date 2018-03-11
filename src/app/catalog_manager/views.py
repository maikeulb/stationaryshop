import sys
from datetime import datetime
from flask import (
    render_template,
    flash, redirect,
    url_for,
    request,
    current_app
)
from flask_login import current_user, login_required
from app.catalog_manager.forms import CatalogItemForm
from app.extensions import login, db
from app.decorators import admin_required, demo_admin_required
from app.catalog_manager import catalog_manager
from app.models import (
    CatalogItem,
    Category,
)


@catalog_manager.before_request
@login_required
@demo_admin_required
def require_login():
    pass


@catalog_manager.route('/')
@catalog_manager.route('/index')
def index():
    catalog_items = CatalogItem.query.all()
    return render_template('catalog_manager/index.html',
                           catalog_items=catalog_items,
                           title='Catalog Items')


@catalog_manager.route('/new', methods=['GET', 'POST'])
def new():
    categories = Category.query \
        .all()
    form = CatalogItemForm()
    form.category.choices = [(c.id, c.name) for c in categories]
    if form.validate_on_submit():
        catalog_item = CatalogItem()
        form.populate_obj(catalog_item)
        try:
            db.session.add(catalog_item)
            db.session.commit()
            flash('Catalog Items added!', 'success')
            print('hi')
            return redirect(url_for('catalog_manager.index'))
        except:
            db.session.rollback()
            flash('Error adding catalog item.', 'danger')

    return render_template('catalog_items/new.html',
                           form=form,
                           title='Catalog Items')


@catalog_manager.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    catalog_item = CatalogItem.query \
        .filter_by(id=id) \
        .first_or_404()
    categories = Category.query \
        .all()
    form = CatalogItemForm(obj=catalog_item)
    form.category_id.choices = [
        (m.id, m.name) for m in categories]
    if form.validate_on_submit():
        form.populate_obj(catalog_item)
        try:
            form.populate_obj(catalog_item)
            db.session.add(catalog_item)
            db.session.commit()
            flash('Catalog Item is updated!', 'success')
            return redirect(url_for('catalog_manager.index'))
        except:
            db.session.rollback()
            flash('Error editing catalog item.', 'danger')

    cateogires = Category.query.all()
    return render_template('catalog_manager/edit.html',
                           cateogires=cateogires,
                           form=form,
                           title='Catalog Items')


@catalog_manager.route('/details/<id>')
def details(id):
    catalog_item = CatalogItem.query \
        .filter_by(id=id) \
        .first_or_404()

    return render_template('catalog_manager/details.html',
                           catalog_item=catalog_item,
                           title='Catalog Items')


@catalog_manager.route('/delete/<id>', methods=['POST'])
def delete(id):
    catalog_item = CatalogItem.query \
        .filter_by(id=id).first_or_404()
    try:
        db.session.delete(catalog_item)
        db.session.commit()
        flash('Delete successfully.', 'success')
    except:
        db.session.rollback()
        flash('Error delete  catalog item.', 'danger')

    return redirect(url_for('catalog_manager.index'))
