# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Medicine(db.Model):
    __tablename__ = 'medicine'

    medicineId = db.Column(db.Integer, primary_key=True, info='药品ID')
    name = db.Column(db.String(50), info='药品名称')
    pay = db.Column(db.Integer, info='费用')
    storage = db.Column(db.Integer, info='库存')
    intro = db.Column(db.String(50), info='简介')
    imgUrl = db.Column(db.String(50), info='药品图片')
    roomName = db.Column(db.String(50), info='科室名称')
    type = db.Column(db.String(20), info='药品种类')
