# coding: utf-8
from init import db
# 操作简介表
# created by lzy

class Taskprocess(db.Model):
    __tablename__ = 'taskprocess'

    taskProcessId = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500))
    imgUrl = db.Column(db.String(50))
    taskId = db.Column(db.Integer)
    process = db.Column(db.Integer)
