# coding: utf-8
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Testpaper(db.Model):
    __tablename__ = 'testpaper'

    testPaperId = db.Column(db.Integer, primary_key=True)
    testId = db.Column(db.Integer)
    paperId = db.Column(db.Integer)
