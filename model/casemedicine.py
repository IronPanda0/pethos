# coding: utf-8
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Casemedicine(db.Model):
    __tablename__ = 'casemedicine'

    caseMId = db.Column(db.Integer, primary_key=True, info='病例药品ID')
    caseId = db.Column(db.Integer, nullable=False, info='病例ID')
    medicineId = db.Column(db.Integer, nullable=False, info='药品ID')
