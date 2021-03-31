# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Caseconsumable(db.Model):
    __tablename__ = 'caseconsumable'

    caseCId = db.Column(db.Integer, primary_key=True, info='病例-收费项目ID')
    caseId = db.Column(db.Integer, info='病例ID')
    consumableId = db.Column(db.Integer, info='收费项目ID')
