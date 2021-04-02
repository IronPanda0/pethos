from flask import Blueprint, request, make_response, render_template, jsonify
from flask_cors import CORS
from sqlalchemy import text
import json
from init import db
from model.disease import Disease
from common.Response import ops_renderErrJSON, ops_renderJSON

disease = Blueprint('diseaseModule', __name__, url_prefix='/disease')


@disease.route("/add", methods=['GET', 'POST'])
def addDisease():
    # html文件修改为新建题目的文件
    if request.method == "GET":
        return render_template("提交疾病.html")
    elif request.method == "POST":
        req = request.values
        # 暂时略过合法性检测
        diseaseName = req['diseaseName']
        categoryName = req['categoryName']
        diseaseNameD = Disease.query.filter_by(diseaseName=diseaseName).first()
        if diseaseNameD:
            return ops_renderErrJSON(msg="相同名字已存在，请再换一个试试")
        # 注册写入数据库
        model_disease = Disease()
        model_disease.diseaseName = diseaseName
        model_disease.categoryName = categoryName
        db.session.add(model_disease)
        db.session.commit()
        # json化data
        temp = {}
        temp["diseaseName"] = diseaseName
        temp["categoryName"] = categoryName
        data = []
        data.append(temp)
        return ops_renderJSON(msg="添加成功", data=data)
    return "添加成功"


@disease.route("/list", methods=['POST'])
def listDisease():
    if request.method == 'POST':
        result = db.session.query(Disease).all()
        temp = {}
        data = []
        if (len(result) != 0):
            for i in result:
                temp["diseaseId"] = i.diseaseId
                temp["diseaseName"] = i.diseaseName
                temp["categoryName"] = i.categoryName
                data.append(temp.copy())
            return ops_renderJSON(msg="查询成功", data=data)
        else:
            return ops_renderErrJSON(msg="查询失败，目前没有疾病")

    return ops_renderJSON(msg="添加成功")

# 根据分类名称返回所有疾病
@disease.route("/search", methods=['POST'])
def searchDisease():
    if request.method == 'POST':
        req = request.values
        categoryName = req['categoryName']
        result = Disease.query.filter_by(categoryName=categoryName).all()
        temp = {}
        data = []
        if (len(result) != 0):
            for i in result:
                temp["diseaseId"] = i.diseaseId
                temp["diseaseName"] = i.diseaseName
                temp["categoryName"] = i.categoryName
                data.append(temp.copy())
            return ops_renderJSON(msg="查询成功", data=data)
        else:
            return ops_renderErrJSON(msg="查询失败，目前该分类没有疾病")

    return ops_renderJSON(msg="添加成功")
