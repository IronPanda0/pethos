# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Fee(db.Model):
    __tablename__ = 'fee'

    feeId = db.Column(db.Integer, primary_key=True, info='收费ID')
    caseId = db.Column(db.Integer, nullable=False, info='病例ID')
    count = db.Column(db.Integer, nullable=False, info='全部费用')
    caseName = db.Column(db.String(50), nullable=False, info='病例名称')
