import pytest
from app import create_app
from app.extensions import db as _db
from webtest import TestApp
from app.models import (
    Category,
    User,
    Permission
)
from ._factories import (
    CatalogItemFactory,
    CategoryFactory,
    CartItemFactory,
    CartFactory,
    OrderFactory,
    OrderDetailFactory,
    UserFactory,
)


@pytest.fixture
def user(db):
    user = UserFactory()
    db.session.commit()
    return user


@pytest.fixture
def category(db):
    category = CategoryFactory()
    db.session.commit()
    return category


@pytest.fixture
def catalog_item(db, category):
    catalog_item = CatalogItemFactory(category_id=category.id)
    db.session.commit()
    return catalog_item


@pytest.fixture
def cart_item(db, catalog_item):
    catalog_item = CartItemFactory(catalog_item_id=catalog_item.id)
    db.session.commit()
    return catalog_item


@pytest.fixture
def order(db, order_detail):
    order = OrderFactory(order_detail_id=order_detail.id)
    db.session.commit()
    return order


@pytest.fixture
def order_detail(db, category):
    order_detail = OrderDetailFactory()
    db.session.commit()
    return order_detail


@pytest.fixture
def cart(db, category):
    cart = CartFactory()
    db.session.commit()
    return cart


@pytest.fixture
def app():
    _app = create_app('config.TestingConfig')
    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture(scope='function')
def testapp(app):
    return TestApp(app)


@pytest.fixture
def db(app):
    _db.app = app
    with app.app_context():
        _db.create_all()

    yield _db

    _db.session.close()
    _db.drop_all()
