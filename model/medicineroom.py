# coding: utf-8
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Medicineroom(db.Model):
    __tablename__ = 'medicineroom'

    Id = db.Column(db.Integer, primary_key=True)
    medicineId = db.Column(db.Integer, nullable=False, info='药品ID')
    roomId = db.Column(db.Integer, nullable=False, info='科室ID')
