from flask import Blueprint, request, make_response, render_template, jsonify
from flask_cors import CORS
from sqlalchemy import text
import json
from init import db
from model.test import Test
from model.paper import Paper
from model.testpaper import Testpaper
from model.paperquestion import Paperquestion
from model.question import Question
from common.Response import ops_renderErrJSON, ops_renderJSON
from datetime import datetime

test = Blueprint('test', __name__, url_prefix='/test')


@test.route("/add", methods=['POST'])
def addTest():
    from init import db
    if request.method == 'POST':
        req = request.values

        testName = req['testName']
        paperId = req['paperId']
        diseaseName = req['diseaseName']
        beginTimeStr = req['beginTime']
        endTimeStr = req['endTime']
        beginTime = datetime.strptime(beginTimeStr, '%Y-%m-%d %H:%M:%S')
        endTime = datetime.strptime(endTimeStr, '%Y-%m-%d %H:%M:%S')

        # 略过数据合法性检测
        testNameD = Test.query.filter_by(testName=testName).first()
        if (testNameD):
            return ops_renderErrJSON(msg="相同考试已存在，请再换一个试试")
        paperD = Paper.query.filter_by(paperId=paperId).first()
        # 写入数据库
        model_test = Test()
        model_test.testName = testName
        model_test.paperName = paperD.paperName
        model_test.beginTime = beginTime
        model_test.endTime = endTime
        model_test.diseaseName = diseaseName
        db.session.add(model_test)
        db.session.commit()
        temp = {}
        temp["testName"] = testName
        temp["paperName"] = paperD.paperName
        temp["beginTime"] = beginTime
        temp["endTime"] = endTime
        temp["diseaseName"] = diseaseName
        data = []
        data.append(temp)
        return ops_renderJSON(msg="添加成功", data=data)
    return "添加成功"


# 前台返回根据病种名返回所有考试
@test.route("/flist", methods=['POST'])
def fListTest():
    if request.method == 'POST':
        res = request.values
        diseaseName = res['diseaseName[0]'] if 'diseaseName[0]' in res else res['diseaseName']
        if (len(diseaseName) == 0):
            result = Test.query.limit(100)
        else:
            result = Test.query.filter_by(diseaseName=diseaseName)
        temp = {}
        data = []
        if (result != None):
            for i in result:
                temp["testId"] = i.testId
                temp["testName"] = i.testName
                temp["paperName"] = i.paperName
                temp["beginTime"] = i.beginTime
                temp["endTime"] = i.endTime
                temp["diseaseName"] = i.diseaseName
                data.append(temp.copy())
            return ops_renderJSON(msg="查询成功", data=data)
        else:
            return ops_renderErrJSON(msg="查询失败，目前没有这场考试")
    return ops_renderJSON(msg="查询成功")


# 根据病种名称返回分页所有考试
@test.route("/list", methods=['POST'])
def listTest():
    if request.method == 'POST':
        res = request.values
        page = int(res['page'])
        per_page = int(res['per_page'])
        diseaseName = res['diseaseName']
        if (page == None):
            page = 1
        if (per_page == None):
            per_page = 10
        if (diseaseName == "all"):
            result = Test.query.limit(per_page).offset((page - 1) * per_page)
        else:
            result = Test.query.filter_by(diseaseName=diseaseName).limit(per_page).offset((page - 1) * per_page)
        temp = {}
        data = []
        if (result != None):
            for i in result:
                temp["testId"] = i.testId
                temp["testName"] = i.testName
                temp["paperName"] = i.paperName
                temp["beginTime"] = i.beginTime
                temp["endTime"] = i.endTime
                temp["diseaseName"] = i.diseaseName
                data.append(temp.copy())
            return ops_renderJSON(msg="查询成功", data=data)
        else:
            return ops_renderErrJSON(msg="查询失败，目前没有这场考试")



# 根据病种名称返回分页所有考试
@test.route("/fuzzy", methods=['POST'])
def fuzzySearchTest():
    if request.method == 'POST':
        res = request.values
        testName = res['testName']
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
        result = db.session.query(Test).filter(Test.testName.like('%%%%%s%%%%' % testName)).limit(per_page).offset(
            (page - 1) * per_page)
        temp = {}
        data = []
        if (result != None):
            for i in result:
                temp["testId"] = i.testId
                temp["testName"] = i.testName
                temp["paperName"] = i.paperName
                temp["beginTime"] = i.beginTime
                temp["endTime"] = i.endTime
                temp["diseaseName"] = i.diseaseName
                data.append(temp.copy())
            return ops_renderJSON(msg="查询成功", data=data)
        else:
            return ops_renderErrJSON(msg="查询失败，目前没有这场考试")

    return ops_renderJSON(msg="查询成功")


# 根据考试名称查询考试
@test.route("/search", methods=['POST'])
def searchTest():
    if request.method == 'POST':
        res = request.values
        testName = res['testName']
        result = Test.query.filter_by(testName=testName).first()
        temp = {}
        data = []
        if (result != None):
            for i in result:
                temp["testId"] = i.testId
                temp["testName"] = i.testName
                temp["paperName"] = i.paperName
                temp["beginTime"] = i.beginTime
                temp["endTime"] = i.endTime
                temp["diseaseName"] = i.diseaseName
                data.append(temp.copy())
            return ops_renderJSON(msg="查询成功", data=data)
        else:
            return ops_renderErrJSON(msg="查询失败，目前没有这场考试")


# 根据testName删除考试
@test.route("/delete", methods=['POST'])
def deleteTest():
    from init import db
    if request.method == 'POST':
        res = request.values
        testId = res['testId']
        testD = db.session.query(Test).filter_by(testId=testId).first()
        if testD == None:
            return ops_renderErrJSON(msg="目前没有该考试，请再次确认")
        testId = testD.testId
        testName = testD.testName
        paperName = testD.paperName
        beginTime = testD.beginTime
        endTime = testD.endTime
        diseaseName = testD.diseaseName
        temp = {}
        temp["testId"] = testId
        temp["testName"] = testName
        temp["paperName"] = paperName
        temp["beginTime"] = beginTime
        temp["endTime"] = endTime
        temp["diseaseName"] = diseaseName
        data = []
        data.append(temp)

        db.session.delete(testD)
        db.session.commit()

        return ops_renderJSON(msg="删除成功", data=data)


@test.route("/update", methods=['POST'])
def updateTest():
    if request.method == 'POST':
        req = request.values
        testId = req['testId']
        testName = req['testName']
        paperName = req['paperName']
        diseaseName = req['diseaseName']
        beginTimeStr = req['beginTime']
        endTimeStr = req['endTime']
        beginTime = datetime.strptime(beginTimeStr, '%Y-%m-%d %H:%M:%S.000Z')
        endTime = datetime.strptime(endTimeStr, '%Y-%m-%d %H:%M:%S.000Z')

        testNameD = db.session.query(Test).filter_by(testName=testName).first()
        if testNameD != None:
            return ops_renderErrJSON(msg="目前已有该考试，请确认后再试试。")
        paperNameD = db.session.query(Paper).filter_by(paperName=paperName).first()
        if paperNameD != None:
            return ops_renderErrJSON(msg="没有该试卷，请确认后再试试。")
        else:
            testU = db.session.query(Test).filter_by(testId=testId).first()
            testU.testName = testName
            testU.paperName = paperName
            testU.diseaseName = diseaseName
            testU.beginTime = beginTime
            testU.endTime = endTime
            db.session.commit()

            # json化data
            temp = {}
            temp["testId"] = testId
            temp["papName"] = testName
            temp["paperName"] = paperName
            temp["diseaseName"] = diseaseName
            temp["beginTime"] = beginTime
            temp["endTime"] = endTime

            data = []
            data.append(temp)
            return ops_renderJSON(msg="修改试卷成功", data=data)


# 根据testId找到PaperID
@test.route("/paper", methods=['POST', 'GET'])
def matchPaper():
    if request.method == 'POST' or 'GET':
        res = request.values
        # 由于前端拿到的数组是字符串数组，需要转化成整型
        testId = res.getlist('testId')
        testId = list(map(int, testId))
        paperIdD = Testpaper.query.filter_by(testId=testId).first()

        if paperIdD is None:
            return ops_renderErrJSON(msg="试卷尚未创建！")
        data = getQuestion(paperId=paperIdD.paperId)
        return ops_renderJSON(msg="成功获取试题集！", data=data)
    return ops_renderErrJSON()


# 根据PaperID返回试题集
def getQuestion(paperId):
    questionIdArray = []
    questionList = Paperquestion.query.filter_by(paperId=paperId)
    if questionList is not None:
        for i in questionList:
            questionIdArray.append(i.questionId)
    data = questionDetail(questionIdArray)
    return data


# 返回试题细节
def questionDetail(questionIdArray):
    data = []
    temp = {}
    for i in questionIdArray:
        questionD = Question.query.filter_by(questionId=i).first()
        temp["questionId"] = i
        temp["questionInfo"] = questionD.questionInfo
        temp["diseaseName"] = questionD.diseaseName
        temp["score"] = questionD.score
        temp["choiceA"] = questionD.choiceA
        temp["choiceB"] = questionD.choiceB
        temp["choiceC"] = questionD.choiceC
        temp["choiceD"] = questionD.choiceD
        data.append(temp.copy())
    return data


# 根据前端返回的数据计算分数
@test.route("/score", methods=["post"])
def countScore():
    if request.method == 'POST':
        res = request.form.to_dict()
        index = int(len(res) / 2)

        questionIdArray = []
        for i in range(index):
            id = res["result[%s][questionId]" % i]
            questionIdArray.append(int(id))
        #     获取试题答案及分值
        score = 0
        sumscore = 0
        data = questionAnswer(questionIdArray)
        for i in data:
            sumscore += i["score"]
            for j in range(index):
                if i["questionId"] == int(res["result[%s][questionId]" % j]) and i["answer"] == int(res["result[%s]["
                                                                                                        "value]" % j]):
                    score += i["score"]
        data = {
            "score": score,
            "sumscore": sumscore
        }
        return ops_renderJSON(msg="分数计算成功", data=data)
    return ops_renderErrJSON()


# 返回试题答案
def questionAnswer(questionIdArray):
    data = []
    temp = {}
    for i in questionIdArray:
        questionD = Question.query.filter_by(questionId=i).first()
        if questionD is not None:
            temp["questionId"] = i
            temp["score"] = questionD.score
            temp["answer"] = questionD.answer
            data.append(temp.copy())
    return data
