# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Consumables(db.Model):
    __tablename__ = 'consumables'

    consumableId = db.Column(db.Integer, primary_key=True, info='收费项目ID')
    name = db.Column(db.String(50, 'utf8_general_ci'), info='项目名称')
    type = db.Column(db.Integer, info='药品1 疫苗2')
    storage = db.Column(db.Integer, info='库存')
    pay = db.Column(db.Integer, info='费用')
