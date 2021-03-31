from flask import Blueprint, request, make_response, render_template, jsonify
from flask_cors import CORS
from sqlalchemy import text
import json
from init import db
from model.disease import Disease
from common.Response import ops_renderErrJSON, ops_renderJSON

disease = Blueprint('diseaseModule', __name__,url_prefix='/caseModule/disease')


@disease.route("/add", methods=['GET', 'POST'])
def addDisease():
    # html文件修改为新建题目的文件
    if request.method == "GET":
        return render_template("提交疾病.html")
    elif request.method == "POST":
        req = request.values
        # 暂时略过合法性检测
        diseaseName= req['diseaseName']
        diseaseNameD = Disease.query.filter_by(diseaseName = diseaseName).first()
        if diseaseNameD:
            return ops_renderErrJSON(msg="相同名字已存在，请再换一个试试")
        # 注册写入数据库
        model_disease = Disease()
        model_disease.diseaseName = diseaseName
        db.session.add(model_disease)
        db.session.commit()
        return ops_renderErrJSON(msg = "添加成功")
    return "添加成功"