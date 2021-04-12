from flask import Blueprint, request, make_response, render_template, jsonify
from flask_cors import CORS
from sqlalchemy import text
import json
from init import db
from model.animal import Animal
from common.Response import ops_renderErrJSON, ops_renderJSON
import decimal

animal = Blueprint('animalModule', __name__, url_prefix='/animal')

from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder


# decimal不能json化
class JSONEncoder(_JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        super(JSONEncoder, self).default(o)


class Flask(_Flask):
    json_encoder = JSONEncoder


@animal.route("/add", methods=['GET', 'POST'])
def addAnimal():
    # html文件修改为新建题目的文件
    if request.method == "GET":
        return render_template("提交宠物.html")
    elif request.method == "POST":
        req = request.values
        # 暂时略过合法性检测
        animalName = req['animalName']
        age = req['age']
        temper = req['temper']
        breathe = req['breathe']
        heartRate = req['heartRate']
        animalNameD = Animal.query.filter_by(animalName=animalName).first()
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
        # json化data
        temp = {}
        temp["animalName"] = animalName
        temp["age"] = age
        temp["temper"] = temper
        temp["breathe"] = breathe
        temp["heartRate"] = heartRate
        data = []
        data.append(temp)
        return ops_renderJSON(msg="添加成功", data=data)
    return "添加成功"


@animal.route("/list", methods=['POST'])
def searchCategory():
    if request.method == 'POST':
        result = db.session.query(Animal).all()
        temp = {}
        data = []
        if (len(result) != 0):
            for i in result:
                temp["animalName"] = i.animalName
                temp["age"] = i.age
                temp["temper"] = i.temper
                temp["breathe"] = i.breathe
                temp["heartRate"] = i.heartRate
                data.append(temp.copy())
            return ops_renderJSON(msg="查询成功", data=data)
        else:
            return ops_renderErrJSON(msg="查询失败，目前没有分类")
