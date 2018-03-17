import sys
from app.extensions import db
from datetime import datetime, timedelta
from hashlib import md5
from time import time
from flask import current_app
from flask_login import UserMixin, AnonymousUserMixin
from app.extensions import bcrypt, login
import jwt
import sys
import json


class Permission:
    GENERAL = 0
    DEMO_ADMINISTER = 1
    ADMINISTER = 2


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    index = db.Column(db.String(64))
    default = db.Column(db.Boolean, default=False, index=True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref='role', lazy='dynamic')

    @staticmethod
    def insert_roles():
        roles = {
            'User': (Permission.GENERAL, 'main', True),
            'DemoAdministrator': (Permission.DEMO_ADMINISTER, 'demo_admin', False),
            'Administrator': (Permission.ADMINISTER, 'admin', False)
        }
        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.permissions = roles[r][0]
            role.index = roles[r][1]
            role.default = roles[r][2]
            db.session.add(role)
        db.session.commit()


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True,
                         unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password = db.Column(db.Binary(128), nullable=True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __init__(self, username, email, role=None, password=None, **kwargs):
        super(User, self).__init__(**kwargs)
        if role:
            self.role = role
        db.Model.__init__(self, username=username, email=email, **kwargs)
        if password:
            self.set_password(password)
        else:
            self.password = None

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, value):
        return bcrypt.check_password_hash(self.password, value)

    def can(self, permissions):
        return self.role.permissions >= permissions

    def is_demo_admin(self):
        return self.can(Permission.DEMO_ADMINISTER)

    def is_admin(self):
        return self.can(Permission.ADMINISTER)


class AnonymousUser(AnonymousUserMixin):
    def can(self, _):
        return False

    def is_admin(self):
        return False

    def is_demo_admin(self):
        return False


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
