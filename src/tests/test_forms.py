from app.account.forms import (
    LoginForm,
    RegistrationForm,
)
from app.catalog.forms import SearchForm


class TestRegistrationForm:
    def test_validate_user_already_registered(self, user):
        form = RegistrationForm(username=user.username, email='foo@bar.com',
                                password='example', confirm='example')
        assert form.validate() is False

    def test_validate_email_already_registered(self, user):
        form = RegistrationForm(username='unique', email=user.email,
                                password='example', confirm='example')
        assert form.validate() is False

    def test_validate_success(self, db):
        form = RegistrationForm(username='newusername', email='new@test.test',
                                password='example', confirm='example')
        assert form.validate() is True


class TestLoginForm:
    def test_validate_success(self, user):
        user.set_password('example')
        form = LoginForm(username=user.username, password='example')
        assert form.validate() is True
        assert form.user == user

    def test_validate_unknown_username(self, db):
        form = LoginForm(username='unknown', password='example')
        assert form.validate() is False
        assert form.user is None

    def test_validate_invalid_password(self, user):
        user.set_password('example')
        form = LoginForm(username=user.username, password='wrongpassword')
        assert form.validate() is False


class TestSearchForm:
    def test_validate_success(self, user):
        form = SearchForm(q='pencil')
        assert form.validate() is True


class CatalogItemForm:
    def test_validate_success(self, user):
        form = CatalogItemForm(
            name='pencil',
            description='amazing',
            image_url="http://image.jpg",
            price=200,
            category_id=1)
        assert form.validate() is True
