from flask import url_for
from datetime import datetime
import pytest


@pytest.mark.usefixtures('db')
class TestOrder:

    def test_get_checkout(self, testapp):
        resp = testapp.get(url_for('order.checkout'))
        assert resp.status_code == 302

    @pytest.mark.skip(reason="not working")
    def test_get_complete(user, client):
        client.login_user()
        resp = client.get(url_for('order.complete'))
        assert resp.status_code == 200

    @pytest.mark.skip(reason="not working")
    def test_get_complete(user, client):
        client.login_user()
        resp = client.post(url_for('order.charge'))
        print(dir(resp))
        assert resp.status_code == 200
