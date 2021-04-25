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
    if request.method == "POST":
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
def listAnimal():
    if request.method == 'POST':
        res = request.values
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
        result = db.session.query(Animal).limit(per_page).offset((page - 1) * per_page)
        temp = {}
        data = []
        if (result != None):
            for i in result:
                temp["animalId"] = i.animalId
                temp["animalName"] = i.animalName
                temp["age"] = i.age
                temp["temper"] = i.temper
                temp["breathe"] = i.breathe
                temp["heartRate"] = i.heartRate
                data.append(temp.copy())
            return ops_renderJSON(msg="查询成功", data=data)
        else:
            return ops_renderErrJSON(msg="查询失败，目前没有宠物")

@animal.route("/fuzzy", methods=['POST'])
def fuzzySearchAnimal():
    if request.method == 'POST':
        res = request.values
        page = res['page']
        per_page = res['per_page']
        animalName = res['animalName']
        if (page == ''):
            page = 1
        else:
            page = int(page)
        if (per_page == ''):
            per_page = 10
        else:
            per_page = int(per_page)
        result = db.session.query(Animal).filter(Animal.animalName.like('%%%%%s%%%%' % animalName)).limit(
            per_page).offset((page - 1) * per_page)
        temp = {}
        data = []
        if (result != None):
            for i in result:
                temp["animalId"] = i.animalId
                temp["animalName"] = i.animalName
                temp["age"] = i.age
                temp["temper"] = i.temper
                temp["breathe"] = i.breathe
                temp["heartRate"] = i.heartRate
                data.append(temp.copy())
            return ops_renderJSON(msg="查询成功", data=data)
        else:
            return ops_renderErrJSON(msg="查询失败，目前没有宠物")

@animal.route("/update", methods=['POST'])
def updateAnimal():
    from init import db
    if request.method == 'POST':
        req = request.values
        animalId = req['animalId']
        animalName = req['animalName']
        age = req['age']
        temper = req['temper']
        breathe = req['breathe']
        heartRate = req['heartRate']
        animalNameD = db.session.query(Animal).filter_by(animalName=animalName).first()
        if animalNameD:
            return ops_renderErrJSON(msg="相同宠物名已经存在，请换一个再试试。")
        else:
            animalU = db.session.query(Animal).filter_by(animalId=animalId).first()

            animalU.animalName = animalName
            animalU.age = age
            animalU.temper = temper
            animalU.breathe = breathe
            animalU.heartRate = heartRate
            db.session.commit()

            # json化data
            temp = {}
            temp["animalId"] = animalId
            temp["animalName"] = animalName
            temp["age"] = age
            temp["temper"] = temper
            temp["breathe"] = breathe
            temp["heartRate"] = heartRate
            data = []
            data.append(temp)
            return ops_renderJSON(msg="修改宠物成功", data=data)


# 根据animalId删除宠物
@animal.route("/delete", methods=['POST'])
def deleteanimal():
    from init import db
    if request.method == 'POST':
        res = request.values
        animalId = res['animalId']
        animalD = db.session.query(Animal).filter_by(animalId=animalId).first()
        if animalD == None:
            return ops_renderErrJSON(msg="目前没有该宠物，请再次确认")
        else:

            temp = {}
            temp["animalId"] = animalD.animalId
            temp["animalName"] = animalD.animalName
            temp["age"] = animalD.age
            temp["temper"] = animalD.temper
            temp["breathe"] = animalD.breathe
            temp["heartRate"] = animalD.heartRate
            data = []
            data.append(temp)
            db.session.delete(animalD)
            db.session.commit()

            return ops_renderJSON(msg="删除宠物成功", data=data)
