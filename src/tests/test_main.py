import pytest
from flask import url_for


def _get_main(testapp, **kwargs):
    return testapp.get(url_for('main.index'), **kwargs)


@pytest.mark.usefixtures('db')
class TestMain:

    def test_get_main(self, testapp):
        resp = _get_main(testapp)
        assert resp.status_code == 200
