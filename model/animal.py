# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Animal(db.Model):
    __tablename__ = 'animal'

    animalId = db.Column(db.Integer, primary_key=True, info='宠物ID')
    animalName = db.Column(db.String(20, 'utf8_general_ci'), nullable=False, info='宠物名称')
    age = db.Column(db.Integer, nullable=False, info='年龄')
    temper = db.Column(db.Float(asdecimal=True), info='体温')
    breathe = db.Column(db.Integer, info='呼吸')
    heartRate = db.Column(db.String(50, 'utf8_general_ci'), info='心率')
