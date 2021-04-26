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
        questionIdList = req.getlist('IdList[]')
        # questionIdList = list(map(int, questionIdList))
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
            scoreD = questionD.score
            model_paperQuestion = Paperquestion()
            model_paperQuestion.questionId = i
            model_paperQuestion.paperId = curPaperId
            db.session.add(model_paperQuestion)
            paperScore += scoreD
            questionCnt += 1
        # paperD = Paper.query.filter_by(paperId=curPaperId).first()
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

@paper.route("/delete", methods=['POST'])
def deletePaper():
    from init import db
    if request.method == 'POST':
        res = request.values
        paperId = res['paperId']
        # diseaseNameD = db.session.query(Disease).filter(Disease.diseaseName == diseaseName).first()
        paperD = db.session.query(Paper).filter_by(paperId=paperId).first()
        if paperD == None:
            return ops_renderErrJSON(msg="目前没有该试卷，请重新确认")
        paperId = paperD.paperId
        paperName = paperD.paperName
        diseaseName = paperD.diseaseName
        sum = paperD.sum
        num = paperD.num
        temp = {}
        temp["paperId"] = paperId
        temp["paperName"] = paperName
        temp["diseaseName"] = diseaseName
        temp["sum"] = sum
        temp["num"] = num
        data = []
        data.append(temp)
        db.session.delete(paperD)
        db.session.commit()
        return ops_renderJSON(msg="删除成功", data=data)


@paper.route("/update", methods=['POST'])
def updatePaper():
    if request.method == 'POST':
        req = request.values
        paperId = req['paperId']
        paperName = req['paperName']
        diseaseName = req['diseaseName']
        paperNameD = db.session.query(Paper).filter_by(paperName=paperName).first()
        if paperNameD:
            return ops_renderErrJSON(msg="相同试卷名已经存在，请换一个再试试。")
        else:
            paperU = db.session.query(Paper).filter_by(paperId=paperId).first()
            paperU.paperName = paperName
            paperU.diseaseName = diseaseName
            db.session.commit()

            # json化data
            temp = {}
            temp["paperId"] = paperId
            temp["paperName"] = paperName
            temp["diseaseName"] = diseaseName
            data = []
            data.append(temp)
            return ops_renderJSON(msg="修改试卷成功", data=data)


@paper.route("/list", methods=['POST'])
def listAnimal():
    if request.method == 'POST':
        res = request.values
        page = res['page']
        per_page = res['per_page']
        if (page == ''):
            page = 1
        else:
            page = int(page)
        if (per_page == ''):
            per_page = 10
        else:
            per_page = int(per_page)
        result = db.session.query(Paper).limit(per_page).offset((page - 1) * per_page)
        temp = {}
        data = []
        if (result != None):
            for i in result:
                temp["paperId"] = i.paperId
                temp["paperName"] = i.paperName
                temp["diseaseName"] = i.diseaseName
                temp["sum"] = i.sum
                temp["num"] = i.num
                data.append(temp.copy())
            return ops_renderJSON(msg="查询成功", data=data)
        else:
            return ops_renderErrJSON(msg="查询失败，目前没有试卷")


@paper.route("/fuzzy", methods=['POST'])
def fuzzySearchAnimal():
    if request.method == 'POST':
        res = request.values
        page = res['page']
        per_page = res['per_page']
        paperName = res['paperName']
        if (page == ''):
            page = 1
        else:
            page = int(page)
        if (per_page == ''):
            per_page = 10
        else:
            per_page = int(per_page)
        result = db.session.query(Paper).filter(Paper.paperName.like('%%%%%s%%%%' % paperName)).limit(per_page).offset(
            (page - 1) * per_page)
        temp = {}
        data = []
        if (result != None):
            for i in result:
                temp["paperId"] = i.paperId
                temp["paperName"] = i.paperName
                temp["diseaseName"] = i.diseaseName
                temp["sum"] = i.sum
                temp["num"] = i.num
                data.append(temp.copy())
            return ops_renderJSON(msg="查询成功", data=data)
        else:
            return ops_renderErrJSON(msg="查询失败，目前没有试卷")
