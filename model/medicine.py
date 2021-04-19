# coding: utf-8
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Medicine(db.Model):
    __tablename__ = 'medicine'

    medicineId = db.Column(db.Integer, primary_key=True, info='药品ID')
    medicineName = db.Column(db.String(50), info='药品名称')
    medicineIntro = db.Column(db.String(50), info='药品效果')
