# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Disease(db.Model):
    __tablename__ = 'disease'

    diseaseId = db.Column(db.Integer, primary_key=True, info='病种ID')
    categoryId = db.Column(db.Integer, info='分类ID')
    diseaseName = db.Column(db.String(50, 'utf8_general_ci'), info='病种名称')
