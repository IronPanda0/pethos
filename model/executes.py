# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Execute(db.Model):
    __tablename__ = 'executes'

    executeId = db.Column(db.Integer, primary_key=True, info='执行类ID')
    name = db.Column(db.String(50), info='项目名称')
    type = db.Column(db.Integer, info='收费种类')
    pay = db.Column(db.Integer, info='费用')
