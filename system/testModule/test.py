from flask import Blueprint, request, make_response, render_template, jsonify
from flask_cors import CORS
from sqlalchemy import text
import json
from init import db
from model.test import Test
from common.Response import ops_renderErrJSON, ops_renderJSON
from datetime import datetime,time

test = Blueprint('test', __name__,url_prefix='/test')

@test.route("/add",methods = ['POST'])
def addTest():
    if request.method == 'POST':
        req = request.values

        testName = req['testName']
        paperName = req['paperName']
        beginTimeStr = req['beginTime']
        endTimeStr = req['endTime']
        diseaseName = req['diseaseName']
        beginTime = datetime.strptime(beginTimeStr, '%Y%m%d %H:%M')
        endTime = datetime.strptime(endTimeStr, '%Y%m%d %H:%M')
        #略过数据合法性检测
        testNameD = Test.query.filter_by(testName = testName).first()
        if(testNameD):
            return ops_renderErrJSON(msg= "相同考试已存在，请再换一个试试")
        #写入数据库
        model_test = Test()
        model_test.testName = testName
        model_test.paperName = paperName
        model_test.beginTime = beginTime
        model_test.endTime = endTime
        model_test.diseaseName = diseaseName
        db.session.add(model_test)
        db.session.commit()
        temp = {}
        temp["testName"] = testName
        temp["paperName"] = paperName
        temp["beginTime"] = beginTime
        temp["endTime"] = endTime
        temp["diseaseName"] = diseaseName
        data = []
        data.append(temp)
        return ops_renderJSON(msg = "添加成功",data = data)
    return "添加成功"

@test.route("/list", methods=['POST'])
def listTest():
    if request.method == 'POST':
        result = Test.query.all()
        temp = {}
        data = []
        if (len(result) != 0):
            for i in result:
                temp["testName"] = i.testName
                temp["paperName"] = i.paperName
                temp["beginTime"] = i.beginTime
                temp["endTime"] = i.endTime
                temp["diseaseName"] = i.diseaseName
                data.append(temp.copy())
            return ops_renderJSON(msg="查询成功", data=data)
        else:
            return ops_renderErrJSON(msg="查询失败，目前没有考试")

# 根据病种名称返回所有考试
@test.route("/search", methods=['POST'])
def searchTest():
    if request.method == 'POST':
        req = request.values
        testName = req['testName']
        result = Test.query.filter_by(testName = testName).all()
        temp = {}
        data = []
        if (len(result) != 0):
            for i in result:
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