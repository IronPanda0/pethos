from flask import Blueprint, request, make_response, render_template, jsonify
from flask_cors import CORS
from sqlalchemy import text
import json
from init import db
from model.paper import Paper
from model.question import Question
from model.paperquestion import Paperquestion
from common.Response import ops_renderErrJSON, ops_renderJSON

paper = Blueprint('paper', __name__, url_prefix='/paper')


@paper.route("/add", methods=['POST'])
def addPaper():
    if request.method == 'POST':
        req = request.values
        # questionIdList = [1,3,4]
        questionIdList = req.getlist('IdList')
        questionIdList = list(map(int, questionIdList))
        paperName = req['paperName']
        diseaseName = req['diseaseName']
        paperD = Paper.query.filter_by(paperName=paperName).first()
        if (paperD):
            return ops_renderErrJSON("目前有该试卷，请重试")
        model_paper = Paper()
        model_paper.paperName = paperName
        model_paper.diseaseName = diseaseName
        db.session.add(model_paper)
        db.session.flush()
        curPaperId = model_paper.paperId
        questionCnt = 0
        paperScore = 0
        for i in questionIdList:
            questionD = Question.query.filter_by(questionId=i).first()
            print(questionD.questionInfo)
            scoreD = questionD.score
            model_paperQuestion = Paperquestion()
            model_paperQuestion.questionId = i
            model_paperQuestion.paperId = curPaperId
            db.session.add(model_paperQuestion)
            paperScore += scoreD
            questionCnt += 1
        paperD = Paper.query.filter_by(paperId=curPaperId).first()
        model_paper.sum = paperScore
        model_paper.num = questionCnt
        db.session.commit()
        temp = {}
        temp["paperName"] = paperName
        temp["diseaseName"] = diseaseName
        temp["sum"] = paperScore
        temp["num"] = questionCnt
        data = []
        data.append(temp)
        return ops_renderJSON(msg="添加成功", data=data)
    return "添加成功"

@paper.route("/delete", methods=['POST'])
def deletePaper():
    from init import db
    if request.method == 'POST':
        res = request.values
        paperName = res['paperName']
        # diseaseNameD = db.session.query(Disease).filter(Disease.diseaseName == diseaseName).first()
        paperD = db.session.query(Paper).filter(Paper.paperName == paperName).first()
        if paperD == None:
            return ops_renderErrJSON(msg="目前没有该试卷，请重新确认")
        diseaseName = paperD.diseaseName
        sum = paperD.sum
        num = paperD.num
        temp = {}
        temp["paperName"] = paperName
        temp["diseaseName"] = diseaseName
        temp["sum"] = sum
        temp["num"] = num
        data = []
        data.append(temp)
        db.session.delete(paperD)
        db.session.commit()

        return ops_renderJSON(msg="删除成功", data=data)
