# coding: utf-8
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Hospital(db.Model):
    __tablename__ = 'hospital'

    hospitalId = db.Column(db.Integer, primary_key=True)
    caseName = db.Column(db.String(50), info='病例名称')
    day = db.Column(db.Integer, info='住院天数')
    pay = db.Column(db.Integer, info='住院费用')
