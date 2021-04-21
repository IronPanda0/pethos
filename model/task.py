# coding: utf-8
from init import db
# 任务表
# created by lzy

class Task(db.Model):
    __tablename__ = 'task'

    taskId = db.Column(db.Integer, primary_key=True)
    taskName = db.Column(db.String(50))
    role = db.Column(db.Integer)
