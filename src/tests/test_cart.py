import pytest
from flask import url_for


def _get_anonymous_cart(testapp, **kwargs):
    return testapp.get(url_for('cart.index'), **kwargs)


@pytest.mark.usefixtures('db')
class TestCart:

    # def test_get_anonymous_cart(self, testapp,  catalog_item):
    #     resp = testapp.get(url_for('cart.index'))
    #     assert resp.status_code == 200

    def test_add_to_anonymous_cart(self, testapp, cart, catalog_item):
        resp = testapp.get(
            url_for('cart.add_to_cart', catalog_item_id=catalog_item.id))
        assert resp.status_code == 302

#     def test_remove_from_anonymous_cart(self, testapp,  catalog_item):
#         testapp.get(
#             url_for('cart.add_to_cart', catalog_item_id=catalog_item.id))
#         resp = testapp.get(
#             url_for('cart.remove_from_cart', catalog_item_id=catalog_item.id))
#         assert resp.status_code == 302
