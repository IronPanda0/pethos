# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Disease(db.Model):
    __tablename__ = 'disease'

    diseaseId = db.Column(db.Integer, primary_key=True, info='病种ID')
    diseaseName = db.Column(db.String(50, 'utf8_general_ci'), nullable=False, info='病种名称')
    categoryName = db.Column(db.String(50), nullable=False, info='分类名称')
