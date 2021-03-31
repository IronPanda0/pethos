from flask import Blueprint, request, make_response, render_template, jsonify
from flask_cors import CORS
from sqlalchemy import text
import json
from init import db
from model.executes import Executes
from common.Response import ops_renderErrJSON, ops_renderJSON

executes = Blueprint('executesModule', __name__,url_prefix='/costModule/executes')


@executes.route("/add", methods=['GET', 'POST'])
def addExecutes():
    # html文件修改为新建题目的文件
    if request.method == "GET":
        return render_template("提交执行类项目.html")
    elif request.method == "POST":
        req = request.values
        # 暂时略过合法性检测
        name= req['name']
        type = req['type']
        pay = req['pay']
        nameD = Executes.query.filter_by(name = name).first()
        if nameD:
            return ops_renderErrJSON(msg="相同项目已存在，请再换一个试试")
        # 注册写入数据库
        model_executes = Executes()
        model_executes.type = type
        model_executes.name = name
        model_executes.pay = pay
        db.session.add(model_executes)
        db.session.commit()
        return ops_renderErrJSON(msg = "添加成功")
    return "添加成功"