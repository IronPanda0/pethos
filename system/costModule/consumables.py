from flask import Blueprint, request, make_response, render_template, jsonify
from flask_cors import CORS
from sqlalchemy import text
import json
from init import db
from model.consumables import Consumables
from common.Response import ops_renderErrJSON, ops_renderJSON

consumables = Blueprint('consumablesModule', __name__,url_prefix='/costModule/consumables')


@consumables.route("/add", methods=['GET', 'POST'])
def addConsumables():
    # html文件修改为新建题目的文件
    if request.method == "GET":
        return render_template("提交消耗类项目.html")
    elif request.method == "POST":
        req = request.values
        # 暂时略过合法性检测
        name= req['name']
        type = req['type']
        storage = req['storage']
        pay = req['pay']
        nameD = Consumables.query.filter_by(name = name).first()
        if nameD:
            return ops_renderJSON(msg="相同项目已存在，请再换一个试试")
        # 注册写入数据库
        model_consumables = Consumables()
        model_consumables.type = type
        model_consumables.name = name
        model_consumables.storage = storage
        model_consumables.pay = pay
        db.session.add(model_consumables)
        db.session.commit()
        return ops_renderErrJSON(msg="添加成功", data=model_consumables)
    return "添加成功"