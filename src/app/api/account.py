from flask import (
    render_template,
    flash,
    g,
    session,
    jsonify,
    redirect,
    url_for,
    request
)
from werkzeug.urls import url_parse
from flask_login import (
    login_user,
    logout_user,
    current_user,
    login_required
)
from app.api import api
from app.models import User, Cart, Category
from app.extensions import login, db
import uuid


@api.route('/account', methods=['POST'])
def login_demo_user():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user.check_password(data['password']):
        login_user(user)
        return jsonify({'result': user.id})
    return jsonify({'result': 0})
