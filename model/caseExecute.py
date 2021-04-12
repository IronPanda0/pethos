# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Caseexecute(db.Model):
    __tablename__ = 'caseexecute'

    caseEId = db.Column(db.Integer, primary_key=True, info='病例-收费项目ID')
    caseId = db.Column(db.Integer, info='病例ID')
    executeId = db.Column(db.Integer, info='收费项目ID')
