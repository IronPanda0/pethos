# coding: utf-8
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()



class Disease(db.Model):
    __tablename__ = 'disease'

    diseaseId = db.Column(db.Integer, primary_key=True, info='病种ID')
<<<<<<< HEAD
<<<<<<< HEAD
    categoryId = db.Column(db.Integer, info='分类ID')
    diseaseName = db.Column(db.String(50, 'utf8_general_ci'), info='病种名称')
=======
    diseaseName = db.Column(db.String(50, 'utf8_general_ci'), nullable=False, info='病种名称')
    categoryName = db.Column(db.String(50), nullable=False, info='分类名称')
>>>>>>> a88316635bfad30e4124c743db3f58697bab070a
=======
    diseaseName = db.Column(db.String(50, 'utf8_general_ci'), nullable=False, info='病种名称')
    categoryName = db.Column(db.String(50), nullable=False, info='分类名称')
>>>>>>> 714c4ca1bc542f77d0daf51e06ce8b29486d32af
