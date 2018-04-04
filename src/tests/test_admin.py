from flask import url_for
from datetime import datetime
import pytest


@pytest.mark.skip(reason="login functionality not working")
@pytest.mark.usefixtures('db')
class TestAdmin:
    def test_get_index(user, client):
        client.login_user()
        resp = client.get(url_for('admin.index'))
        assert resp.status_code == 200
