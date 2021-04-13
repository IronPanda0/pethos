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

        # 随机生成试卷
        # # 略过数据合法性检测
        # paperNameD = Paper.query.filter_by(paperName=paperName).first()
        # if (paperNameD):
        #     return ops_renderErrJSON(msg="相同试卷已存在，请再换一个试试")
        # diseaseNameD = Question.query.filter_by(diseaseName=diseaseName).first()
        # model_paper = Paper()
        # model_paper.paperName = paperName
        # model_paper.diseaseName = diseaseName
        # db.session.add(model_paper)
        # db.session.flush()
        # # db.session.commit()
        # curPaperId = model_paper.paperId
        # if (diseaseNameD):
        #     result = Question.query.filter_by(diseaseName=diseaseName).all()
        # temp = {}
        # data = []
        # cnt = 0
        # sum = 0
        # if (len(result) != 0):
        #     if (len(result) <= num):
        #         model_paperquestion = Paperquestion()
        #         model_paper.sum = 0
        #         for i in result:
        #             model_paperquestion.questionId = i.questionId
        #             model_paperquestion.testId = curPaperId
        #             db.session.add(model_paperquestion)
        #             model_paper.sum += i.score
        #             temp["questionId"] = i.questionId
        #             temp["questionInfo"] = i.questionInfo
        #             temp["answer"] = i.answer
        #             temp["choiceA"] = i.choiceA
        #             temp["choiceB"] = i.choiceB
        #             temp["choiceC"] = i.choiceC
        #             temp["choiceD"] = i.choiceD
        #             temp["score"] = i.score
        #             temp["diseaseName"] = i.diseaseName
        #             data.append(temp.copy())
        #     elif (len(result)>0):
        #         model_paper.sum = 0
        #         for i in result:
        #             model_paper.sum += i.score
        #             temp["questionId"] = i.questionId
        #             temp["questionInfo"] = i.questionInfo
        #             temp["answer"] = i.answer
        #             temp["choiceA"] = i.choiceA
        #             temp["choiceB"] = i.choiceB
        #             temp["choiceC"] = i.choiceC
        #             temp["choiceD"] = i.choiceD
        #             temp["score"] = i.score
        #             temp["diseaseName"] = i.diseaseName
        #             data.append(temp.copy())
        #             if cnt >= num:
        #                 cnt += 1
        #                 break
        #     db.session.commit()
        #     return ops_renderJSON(msg="试卷生成成功", data=data)
        # else:
        #     db.session.commit()
        #     return ops_renderErrJSON(msg="试卷生成失败，目前该病种没有试题")

#
#
#         #写入数据库
#         model_paper = Paper()
#         model_paper.paperName = paperName
#         model_paper.diseaseName = diseaseName
#         model_paper.
#         db.session.add(model_paper)
#         db.session.commit()
#         temp = {}
#         temp["paperName"] = paperName
#         temp["paperName"] = paperName
#         temp["beginTime"] = beginTime
#         temp["endTime"] = endTime
#         data = []
#         data.append(temp)
#         return ops_renderJSON(msg = "添加成功",data = data)
#     return "添加成功"
#
# @paper.route("/list", methods=['POST'])
# def searchPaper():
#     if request.method == 'POST':
#         result = Paper.query.all()
#         temp = {}
#         data = []
#         if (len(result) != 0):
#             for i in result:
#                 temp["paperName"] = i.paperName
#                 temp["paperName"] = i.paperName
#                 temp["beginTime"] = i.beginTime
#                 temp["endTime"] = i.endTime
#                 data.append(temp.copy())
#             return ops_renderJSON(msg="查询成功", data=data)
#         else:
#             return ops_renderErrJSON(msg="查询失败，目前没有考试")
#
