# coding: utf-8
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Question(db.Model):
    __tablename__ = 'question'

    questionId = db.Column(db.Integer, primary_key=True, info='问题ID')
    questionInfo = db.Column(db.String(500, 'utf8_general_ci'), info='题干')
    answer = db.Column(db.Integer, info='答案')
    diseaseName = db.Column(db.String(50, 'utf8_general_ci'), info='所属病种名称')
    score = db.Column(db.Integer, info='分值')
    choiceA = db.Column(db.String(50), info='选项A')
    choiceB = db.Column(db.String(50), info='选项B')
    choiceC = db.Column(db.String(50), info='选项C')
    choiceD = db.Column(db.String(50), info='选项D')
