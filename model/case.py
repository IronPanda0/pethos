# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Case(db.Model):
    __tablename__ = 'caseModule'

    caseId = db.Column(db.Integer, primary_key=True, info='病例ID')
    caseName = db.Column(db.String(50, 'utf8_general_ci'), info='病例名称')
    animalName = db.Column(db.String(20), info='宠物名称')
    diseaseName = db.Column(db.String(50, 'utf8_general_ci'), info='病种名称')
    diseaseinfo = db.Column(db.String(500, 'utf8_general_ci'), info='文字简介')
    videoUrl = db.Column(db.String(50, 'utf8_general_ci'), info='视频信息')
    imageUrl = db.Column(db.String(50, 'utf8_general_ci'), info='图片信息')
