from flask import Blueprint, request, make_response, render_template, jsonify
from flask_cors import CORS
from sqlalchemy import text
import json
from common.Response import ops_renderErrJSON, ops_renderJSON
from model.disease import Disease
from model.case import Case
disease = Blueprint('diseaseModule', __name__, url_prefix='/disease')


@disease.route("/add", methods=['POST'])
def addDisease():
    from init import db
    # html文件修改为新建题目的文件
    if request.method == "POST":
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


# 根据分类名称返回疾病
@disease.route("/list", methods=['POST'])
def listDisease():
    if request.method == 'POST':
        res = request.values
        categoryName = res['categoryName']
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
        if (categoryName == 'all'):
            result = Disease.query.limit(per_page).offset((page - 1) * per_page)
        else:
            result = Disease.query.filter_by(categoryName=categoryName).limit(per_page).offset((page - 1) * per_page)
        temp = {}
        data = []
        if (result.count() != 0):
            for i in result:
                temp["diseaseId"] = i.diseaseId
                temp["diseaseName"] = i.diseaseName
                temp["categoryName"] = i.categoryName
                data.append(temp.copy())
            return ops_renderJSON(msg="查询成功", data=data)
        else:
            return ops_renderErrJSON(msg="查询失败，目前该分类没有疾病")


@disease.route("/fuzzy", methods=['POST'])
def fuzzySearchDisease():
    from init import db
    if request.method == 'POST':
        res = request.values
        diseaseName = res['diseaseName']
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
        result = db.session.query(Disease).filter(Disease.diseaseName.like('%%%%%s%%%%' % diseaseName)).limit(
            per_page).offset((page - 1) * per_page)
        temp = {}
        data = []
        if (result.count() != 0):
            for i in result:
                temp["diseaseId"] = i.diseaseId
                temp["diseaseName"] = i.diseaseName
                temp["categoryName"] = i.categoryName
                data.append(temp.copy())
            return ops_renderJSON(msg="查询成功", data=data)
        else:
            return ops_renderErrJSON(msg="查询失败，目前没有疾病")

# 根据diseaeName删除病种
@disease.route("/delete", methods=['POST'])
def deleteDisease():
    from init import db
    if request.method == 'POST':
        res = request.values
        diseaseName = res['diseaseName']
        diseaseNameD = db.session.query(Disease).filter(Disease.diseaseName == diseaseName).first()
        if diseaseNameD == None:
            return ops_renderErrJSON(msg="目前没有该病种，请再次确认")
        categoryName = diseaseNameD.categoryName
        temp = {}
        temp["diseaseName"] = diseaseName
        temp["categoryName"] = categoryName
        data = []
        data.append(temp)

        db.session.delete(diseaseNameD)
        db.session.commit()

        return ops_renderJSON(msg="删除成功", data=data)


@disease.route("/search", methods=['POST'])
def searchDisease():
    from init import db
    if request.method == 'POST':
        res = request.values
        diseaseName = res['diseaseName']
        diseaseNameD = db.session.query(Disease).filter(Disease.diseaseName == diseaseName).first()
        if diseaseNameD == None:
            return ops_renderErrJSON(msg="目前没有该病种，请再次确认")
        categoryName = diseaseNameD.categoryName
        result = db.session.query(Case).filter(Case.diseaseName == diseaseName).all()
        caseNum = len(result)
        temp = {}
        temp["categoryName"] = categoryName
        temp["caseNum"] = caseNum
        data = []
        data.append(temp)
        return ops_renderJSON(msg="查询成功", data=data)
