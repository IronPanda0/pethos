# coding: utf-8
from init import db




class Paper(db.Model):
    __tablename__ = 'paper'

    paperId = db.Column(db.Integer, primary_key=True, info='试卷ID')
    paperName = db.Column(db.String(50), info='试卷名称')
    sum = db.Column(db.Integer, info='试卷总分')
    num = db.Column(db.Integer, info='试卷题数')
    diseaseId = db.Column(db.Integer, info='所属病种ID')
    diseaseName = db.Column(db.String(50, 'utf8_general_ci'), info='所属病种名称')
