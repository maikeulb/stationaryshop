from flask import url_for
from datetime import datetime
import pytest


@pytest.mark.usefixtures('db')
class TestApi:

    def test_get_catalog_items(self, testapp):
        resp = testapp.get(url_for('api.get_catalog_items'))
        assert resp.status_code == 200

    def test_delete_catalog_item(self, testapp):
        resp = testapp.delete(url_for('api.delete_catalog_item', id=1))
        assert resp.status_code == 204
