import pytest
from flask import url_for


@pytest.mark.usefixtures('db')
class TestAccount:

    def test_get_register(self, user, testapp):
        res = testapp.get(url_for('account.register'))
        assert res.status_code == 200

    def test_get_login(self, user, testapp):
        res = testapp.get(url_for('account.login'))
        assert res.status_code == 200

    def test_can_register(self, user, testapp):
        res = testapp.post(url_for('account.register', data=user))
        assert res.status_code == 200

    def test_can_login(self, user, testapp):
        res = testapp.post(url_for('account.register', data=user))
        res = testapp.post(url_for('account.login', data=user))
        assert res.status_code == 200
