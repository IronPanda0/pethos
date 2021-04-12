# from flask import Blueprint, request, make_response, render_template, jsonify
# from flask_cors import CORS
# from sqlalchemy import text
# import json
# from init import db
# from model.paper import Paper
# from model.question import Question
# from common.Response import ops_renderErrJSON, ops_renderJSON
#
# paper = Blueprint('paper', __name__,url_prefix='/paper')
#
# @paper.route("/add",methods = ['POST'])
# def addPaper():
#     if request.method == 'POST':
#         req = request.values
#
#         num = req['num']
#         paperName = req['papaerName']
#         diseaseName = req['diseaseName']
#         #略过数据合法性检测
#         paperNameD = Paper.query.filter_by(paperName = paperName).first()
#         if(paperNameD):
#             return ops_renderErrJSON(msg= "相同试卷已存在，请再换一个试试")
#         result = Question.query.filter_by(diseaseName = diseaseName).all()
#         if(len(result)!=0):
#             tempQ = {}
#             for i in result:
#
#
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
