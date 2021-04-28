# coding: utf-8
from init import db



class Testuser(db.Model):
    __tablename__ = 'testuser'

    testUser = db.Column(db.Integer, primary_key=True, info='????ID')
    testId = db.Column(db.Integer, info='??ID')
    userId = db.Column(db.Integer, info='??ID')
    score = db.Column(db.Integer)
