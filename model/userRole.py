# coding: utf-8
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Userrole(db.Model):
    __tablename__ = 'userrole'

    userRoleId = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(20), nullable=False)
    role = db.Column(db.String(20), nullable=False, info='前台，医助，医师')
    content = db.Column(db.String(500))
    duty = db.Column(db.String(500))
    process = db.Column(db.String(500))
