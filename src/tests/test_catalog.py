from flask import url_for
from datetime import datetime
import pytest


def _get_catalog_items(testapp, **kwargs):
    return testapp.get(url_for('main.index'), **kwargs)


def _get_catalog_item(testapp, id, **kwargs):
    return testapp.get(url_for('main.index', id=id), **kwargs)


@pytest.mark.usefixtures('db')
class TestCatalog:

    def test_get_catalog_items(self, testapp):
        resp = _get_catalog_items(testapp)
        assert resp.status_code == 200

    def test_get_catalog_item(self, testapp):
        resp = _get_catalog_item(testapp, 1)
        assert resp.status_code == 200
