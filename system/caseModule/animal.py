from flask import Blueprint, request, make_response, render_template, jsonify
from flask_cors import CORS
from sqlalchemy import text
import json
from init import db
from model.animal import Animal
from common.Response import ops_renderErrJSON, ops_renderJSON

animal = Blueprint('animalModule', __name__,url_prefix='/caseModule/animal')


@animal.route("/add", methods=['GET', 'POST'])
def addAnimal():
    # html文件修改为新建题目的文件
    if request.method == "GET":
        return render_template("提交宠物.html")
    elif request.method == "POST":
        req = request.values
        # 暂时略过合法性检测
        animalName= req['animalName']
        age = req['age']
        temper = req['temper']
        breathe = req['breathe']
        heartRate = req['heartRate']
        animalNameD = Animal.query.filter_by(animalName = animalName).first()
        if animalNameD:
            return ops_renderErrJSON(msg="相同名字已存在，请再换一个试试")
        # 注册写入数据库
        model_animal = Animal()
        model_animal.age = age
        model_animal.animalName = animalName
        model_animal.temper = temper
        model_animal.breathe = breathe
        model_animal.heartRate = heartRate
        db.session.add(model_animal)
        db.session.commit()
        return ops_renderErrJSON(msg = "添加成功")
    return "添加成功"