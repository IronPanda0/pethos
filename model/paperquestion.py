# coding: utf-8
from init import db



class Paperquestion(db.Model):
    __tablename__ = 'paperquestion'

    paperQuestionId = db.Column(db.Integer, primary_key=True, info='考试试题ID')
    paperId = db.Column(db.Integer, info='试卷ID')
    questionId = db.Column(db.Integer, info='问题ID')
