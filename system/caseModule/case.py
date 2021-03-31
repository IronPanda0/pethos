from flask import Blueprint, request, make_response, render_template, jsonify
from flask_cors import CORS
from sqlalchemy import text
import json
from init import db
from model.case import Case
from common.Response import ops_renderErrJSON, ops_renderJSON

case = Blueprint('caseModule', __name__,url_prefix='/caseModule/case')


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
        diseaseInfo = req['diseaseInfo']
        videoUrl = req['videoUrl']
        imgUrl = req['imgUrl']
        caseNameD = Case.query.filter_by(caseName = caseName).first()
        if caseNameD:
            return ops_renderErrJSON(msg="相同题干已存在，请再换一个试试")
        # 注册写入数据库
        model_case = Case()
        model_case.diseaseinfo = diseaseInfo
        model_case.animalName = animalName
        model_case.videoUrl = videoUrl
        model_case.imageUrl = imgUrl
        db.session.add(model_case)
        db.session.commit()
        return ops_renderErrJSON(msg = "添加成功")
    return "添加成功"