from flask import url_for
from datetime import datetime
import pytest


def _get_anonymous_cart(testapp, **kwargs):
    return testapp.get(url_for('cart.index'), **kwargs)


@pytest.mark.usefixtures('db')
class TestCart:

    def test_get_anonymous_cart(self, testapp):
        resp = _get_anonymous_cart(testapp)
        assert resp.status_code == 200
