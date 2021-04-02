from flask import Blueprint, request, make_response, render_template, jsonify
from flask_cors import CORS
from sqlalchemy import text
import json
from init import db
from model.case import Case
from common.Response import ops_renderErrJSON, ops_renderJSON

case = Blueprint('caseModule', __name__, url_prefix='/case')


@case.route("/add", methods=['GET', 'POST'])
def addCase():
    # html文件修改为新建题目的文件
    if request.method == "GET":
        return render_template("提交病例.html")
    elif request.method == "POST":
        req = request.values
        # 暂时略过合法性检测
        caseName= req['caseName']
        animalName = req['animalName']
        diseaseName = req['diseaseName']
        diseaseInfo = req['diseaseInfo']
        videoUrl = req['videoUrl']
        imageUrl = req['imageUrl']
        caseNameD = Case.query.filter_by(caseName=caseName).first()
        if caseNameD:
            return ops_renderErrJSON(msg="相同题干已存在，请再换一个试试")
        # 注册写入数据库
        model_case = Case()
        model_case.caseName = caseName
        model_case.diseaseName = diseaseName
        model_case.diseaseinfo = diseaseInfo
        model_case.animalName = animalName
        model_case.videoUrl = videoUrl
        model_case.imageUrl = imageUrl
        db.session.add(model_case)
        db.session.commit()
        # json化data
        temp = {}
        temp["caseName"] = caseName
        temp["diseaseName"] = diseaseName
        temp["diseaseInfo"] = diseaseInfo
        temp["animalName"] = animalName
        temp["videoUrl"] = videoUrl
        temp["imageUrl"] = imageUrl
        data = []
        data.append(temp)
        return ops_renderJSON(msg="添加成功", data=data)
    return "添加成功"


@case.route("/list", methods=['POST'])
def searchCase():
    if request.method == 'POST':
        result = db.session.query(Case).all()
        temp = {}
        data = []
        if (result != None):
            for i in result:
                temp["caseName"] = i.caseName
                temp["diseaseName"] = i.diseaseName
                temp["diseaseInfo"] = i.diseaseInfo
                temp["animalName"] = i.animalName
                temp["videoUrl"] = i.videoUrl
                temp["imageUrl"] = i.imageUrl
                data.append(temp.copy())
            return ops_renderJSON(msg="查询成功", data=data)
        else:
            return ops_renderErrJSON(msg="查询失败，目前没有分类")
