from flask_login import UserMixin

from .db import db


class User(db.Model, UserMixin):
    __tablename__ = 'userTable'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(45), nullable=False, unique=True)
    name = db.Column(db.String(45), nullable=False, default='')
    email = db.Column(db.String(45), nullable=True)
    admin_flag = db.Column(db.Boolean, name='adminFlag', default=False, nullable=False)
