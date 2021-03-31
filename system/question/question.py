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
        model_question.diseaseName = diseaseName
        db.session.add(model_question)
        db.session.commit()
        return ops_renderErrJSON(msg = "添加成功")
    return "添加成功"