# coding: utf-8
from init import db
# 物品简介表
# created by lzy

class Item(db.Model):
    __tablename__ = 'item'

    itemId = db.Column(db.Integer, primary_key=True)
    roomId = db.Column(db.Integer)
    itemName = db.Column(db.String(20))
    intro = db.Column(db.String(500))
    videoUrl = db.Column(db.String(50))
