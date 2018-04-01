import pytest

from app import create_app
from app.extensions import db as _db
from webtest import TestApp
from datetime import date
from random import choice, shuffle, sample
from app.models import Category, CatalogItem, Role, User, Permission
from .factories import UserFactory


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
        _db.create_all()

        # def seed_users():
        # Role.insert_roles()

        # demo = User(
        #     username='demo',
        #     password='P@ssw0rd!'
        #     email=Config.DEMO_EMAIL,
        #     role=Role.query.filter_by(permissions=Permission.GENERAL).first())
        # demo_admin = User(
        #     username='demo_admin',
        #     password=Config.DEMO_ADMIN_PASSWORD,
        #     email=Config.DEMO_ADMIN_EMAIL,
        #     role=Role.query.filter_by(permissions=Permission.DEMO_ADMINISTER).first())
        # admin = User(
        #     username='admin',
        #     password=Config.ADMIN_PASSWORD,
        #     email=Config.ADMIN_EMAIL,
        #     role=Role.query.filter_by(permissions=Permission.ADMINISTER).first())

        # db.session.add(demo)
        # db.session.add(demo_admin)
        # db.session.add(admin)

        def seed_categories():
            Role.insert_roles()

            notebooks = Category(
                name='notebooks')
            pens = Category(
                name='pens and pencils')
            desk = Category(
                name='desk accessories')

            _db.session.add(notebooks)
            _db.session.add(pens)
            _db.session.add(desk)

        def seed_catalog():
            paper_note = CatalogItem(
                name='Paper Note',
                description="120 sheets",
                image_url="http://www.muji.us/store/pub/media/catalog/product/cache/1/image/700x560/e9c3970ab036de70892d86c6d221abfe/4/9/4934761910017.jpg",
                price=20,
                category_id=1)

            double_ring = CatalogItem(
                name='Plantation Double Ring Note',
                description="80 sheets",
                image_url="http://www.muji.us/store/pub/media/catalog/product/cache/1/image/700x560/e9c3970ab036de70892d86c6d221abfe/4/5/4547315264971.jpg",
                price=2.5,
                category_id=1)

            paper_note_set = CatalogItem(
                name='Planation Paper Note 5PCS/Set',
                description="30 sheets/book",
                image_url="http://www.muji.us/store/pub/media/catalog/product/cache/1/image/700x560/e9c3970ab036de70892d86c6d221abfe/4/5/4548076316145_400_2.jpg",
                price=3.5,
                category_id=1)

            recyle_paper = CatalogItem(
                name='Recycle Paper Double Ring Note',
                description="80 sheets",
                image_url="http://www.muji.us/store/pub/media/catalog/product/cache/1/image/700x560/e9c3970ab036de70892d86c6d221abfe/4/5/4548718218905_1260_1.jpg",
                price=3,
                category_id=1)

            _db.session.add(paper_note)
            _db.session.add(double_ring)
            _db.session.add(paper_note_set)
            _db.session.add(recyle_paper)

            colored_pencils = CatalogItem(
                name='12 Colored Pencils',
                description="Material: Cedar",
                image_url="http://www.muji.us/store/pub/media/catalog/product/cache/1/image/700x560/e9c3970ab036de70892d86c6d221abfe/4/9/4934761512570_1260.jpg",
                price=5,
                category_id=2)

            ballpoint_pens = CatalogItem(
                name='Gel-Ink BallPoint Pen 6PCS/SET',
                description="Pen Nib: 0.38mm",
                image_url="http://www.muji.us/store/pub/media/catalog/product/cache/1/image/e9c3970ab036de70892d86c6d221abfe/4/5/4548718990009_400.jpg",
                price=8,
                category_id=2)

            hexa_pen = CatalogItem(
                name='10 Colors Hexa Pen Set Minia',
                description="Material: Polyproplene",
                image_url="http://www.muji.us/store/pub/media/catalog/product/cache/1/image/700x560/e9c3970ab036de70892d86c6d221abfe/4/5/4548718963027.jpg",
                price=5,
                category_id=2)

            _db.session.add(colored_pencils)
            _db.session.add(ballpoint_pens)
            _db.session.add(hexa_pen)

            calculator = CatalogItem(
                name='Calculator',
                description="Color: Black",
                image_url="http://www.muji.us/store/pub/media/catalog/product/cache/1/image/700x560/e9c3970ab036de70892d86c6d221abfe/4/5/4548076151616_400.jpg",
                price=25,
                category_id=3)

            correction_tape = CatalogItem(
                name='Correction Tape',
                description="Dimensions: 5mmx10cm",
                image_url="http://www.muji.us/store/pub/media/catalog/product/cache/1/image/700x560/e9c3970ab036de70892d86c6d221abfe/4/9/4934761155067_400.jpg",
                price=8,
                category_id=3)

            hole_puncher = CatalogItem(
                name='2 Hole Puncher',
                description="Maximum Capacity:10c",
                image_url="http://www.muji.us/store/pub/media/catalog/product/cache/1/image/700x560/e9c3970ab036de70892d86c6d221abfe/4/5/4549337355521.jpg",
                price=5.5,
                category_id=3)

            _db.session.add(calculator)
            _db.session.add(correction_tape)
            _db.session.add(hole_puncher)

        # seed_users()
        seed_categories()
        seed_catalog()
        _db.session.commit()

    yield _db

    _db.session.close()
    _db.drop_all()


@pytest.fixture
def user(db):
    """A user for the tests."""
    user = UserFactory(password='myprecious')
    db.session.commit()
    return user
