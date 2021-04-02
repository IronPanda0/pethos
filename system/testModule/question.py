from flask import Blueprint, request, make_response, render_template, jsonify
from flask_cors import CORS
from sqlalchemy import text
import json
from init import db
from model.question import Question
from common.Response import ops_renderErrJSON, ops_renderJSON

question = Blueprint('question', __name__,url_prefix='/question')


@question.route("/add", methods=['GET', 'POST'])
def addQuestion():
    # html文件修改为新建题目的文件
    if request.method == "GET":
        return render_template("提交题目.html")
    elif request.method == "POST":
        req = request.values
        # 暂时略过合法性检测
        questionInfo = req['questionInfo']
        answer = req['answer']
        diseaseName = req['diseaseName']
        score = req['score']
        choiceA = req['choiceA']
        choiceB = req['choiceB']
        choiceC = req['choiceC']
        choiceD = req['choiceD']
        questionInfoD = Question.query.filter_by(questionInfo = questionInfo).first()
        if questionInfoD:
            return ops_renderErrJSON(msg="相同题干已存在，请再换一个试试")
        # 注册写入数据库
        model_question = Question()
        model_question.questionInfo = questionInfo
        model_question.choiceA = choiceA
        model_question.choiceB = choiceB
        model_question.choiceC = choiceC
        model_question.choiceD = choiceD
        model_question.answer = answer
        model_question.score = score
        model_question.diseaseName = diseaseName
        db.session.add(model_question)
        db.session.commit()
        # json化data
        temp = {}
        temp["questionInfo"] = questionInfo
        temp["answer"] = answer
        temp["choiceA"] = choiceA
        temp["choiceB"] = choiceB
        temp["choiceC"] = choiceC
        temp["choiceD"] = choiceD
        temp["score"] = score
        temp["diseaseName"] = diseaseName
        data = []
        data.append(temp)
        return ops_renderJSON(msg="添加成功", data=data)
    return "添加成功"


@question.route("/list", methods=['POST'])
def listQuestion():
    if request.method == 'POST':
        result = Question.query.all()
        temp = {}
        data = []
        if (result != None):
            for i in result:
                temp["questionInfo"] = i.questionInfo
                temp["answer"] = i.answer
                temp["choiceA"] = i.choiceA
                temp["choiceB"] = i.choiceB
                temp["choiceC"] = i.choiceC
                temp["choiceD"] = i.choiceD
                temp["score"] = i.score
                temp["diseaseName"] = i.diseaseName
                data.append(temp.copy())
            return ops_renderJSON(msg="查询成功", data=data)
        else:
            return ops_renderErrJSON(msg="查询失败，目前没有题目")

# 根据病种名称返回所有试题
@question.route("/search", methods=['POST'])
def searchQuestion():
    if request.method == 'POST':
        req = request.values
        diseaseName = req['diseaseName']
        result = Question.query.filter_by(diseaseName = diseaseName).all()
        temp = {}
        data = []
        if (len(result) != 0):
            for i in result:
                temp["questionInfo"] = i.questionInfo
                temp["answer"] = i.answer
                temp["choiceA"] = i.choiceA
                temp["choiceB"] = i.choiceB
                temp["choiceC"] = i.choiceC
                temp["choiceD"] = i.choiceD
                temp["score"] = i.score
                temp["diseaseName"] = i.diseaseName
                data.append(temp.copy())
            return ops_renderJSON(msg="查询成功", data=data)
        else:
            return ops_renderErrJSON(msg="查询失败，目前该病种没有试题")

    return ops_renderJSON(msg="查询成功")