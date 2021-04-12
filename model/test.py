# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Test(db.Model):
    __tablename__ = 'test'

    testId = db.Column(db.Integer, primary_key=True, info='考试ID')
    testName = db.Column(db.String(50), info='考试名称')
    paperName = db.Column(db.String(50), info='试卷名称')
    beginTime = db.Column(db.DateTime, info='开始时间')
    endTime = db.Column(db.DateTime, info='结束时间')
    diseaseName = db.Column(db.String(50), info='相关病种')
