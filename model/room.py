# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Room(db.Model):
    __tablename__ = 'room'

    roomId = db.Column(db.Integer, primary_key=True, info='科室ID')
    intro = db.Column(db.String(500, 'utf8_general_ci'), info='介绍')
    employee = db.Column(db.String(20), info='负责人姓名')
    roomName = db.Column(db.String(20), info='科室名称')
    imgUrl = db.Column(db.String(100, 'utf8_general_ci'), info='科室图片')
