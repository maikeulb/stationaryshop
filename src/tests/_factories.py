from factory import PostGenerationMethodCall, Sequence
from factory.alchemy import SQLAlchemyModelFactory
from app.extensions import db
from app.models import (
    Cart,
    CartItem,
    CatalogItem,
    Category,
    Order,
    OrderDetail,
    User
)


class BaseFactory(SQLAlchemyModelFactory):
    class Meta:
        abstract = True
        sqlalchemy_session = db.session


class UserFactory(BaseFactory):
    id = Sequence(lambda n: n)
    username = Sequence(lambda n: 'user{0}'.format(n))
    email = Sequence(lambda n: 'user{0}@example.com'.format(n))
    password = PostGenerationMethodCall('set_password', 'example')

    class Meta:
        model = User


class CatalogItemFactory(BaseFactory):
    id = Sequence(lambda n: n)
    name = Sequence(lambda n: 'user{0}'.format(n))
    description = Sequence(lambda n: 'user{0}@example.com'.format(n))
    image_url = Sequence(lambda n: 'user{0}@example.com'.format(n))
    price = Sequence(lambda n: n)
    category_id = Sequence(lambda n: n)

    class Meta:
        model = CatalogItem


class CategoryFactory(BaseFactory):
    id = Sequence(lambda n: n)
    name = Sequence(lambda n: 'user{0}'.format(n))

    # catalog_items = SubFactory(CatalogItemFactory)

    class Meta:
        model = Category


class CartItemFactory(BaseFactory):
    id = Sequence(lambda n: n)
    amount = Sequence(lambda n: n)
    cart_id = Sequence(lambda n: n)
    catalog_item_id = Sequence(lambda n: n)

    # catalog_item = SubFactory(CatalogItemFactory)

    class Meta:
        model = CartItem


class OrderDetailFactory(BaseFactory):
    id = Sequence(lambda n: n)
    amount = Sequence(lambda n: n)
    price = Sequence(lambda n: n)

    # catalog_item = SubFactory(CatalogItemFactory)

    class Meta:
        model = OrderDetail


class OrderFactory(BaseFactory):
    id = Sequence(lambda n: n)
    order_total = Sequence(lambda n: n)
    order_detail_id = Sequence(lambda n: n)

    # order_lines = SubFactory(OrderDetailFactory)

    class Meta:
        model = Order


class CartFactory(BaseFactory):
    id = Sequence(lambda n: n)
    # cart_items = SubFactory(CartItemFactory)

    class Meta:
        model = Cart
