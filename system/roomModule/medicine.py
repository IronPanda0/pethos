from flask import Blueprint, request, make_response, render_template, jsonify
from flask_cors import CORS
from sqlalchemy import text
import json
from init import db
from model.medicine import Medicine
from common.Response import ops_renderErrJSON, ops_renderJSON
from datetime import datetime, time

medicine = Blueprint('medicine', __name__, url_prefix='/medicine')


@medicine.route("/add", methods=['POST'])
def addMedicine():
    if request.method == "GET":
        return render_template("新增medicine.html")
    elif request.method == "POST":
        req = request.values
        medicineName = req['medicineName']
        medicineIntro = req['medicineIntro']
        # 略过数据合法性检测
        medicineNameD = Medicine.query.filter_by(medicineName=medicineName).first()
        if (medicineNameD):
            return ops_renderErrJSON(msg="相同药品已存在，请再换一个试试")
        # 写入数据库
        model_medicine = Medicine()
        model_medicine.medicineName = medicineName
        model_medicine.medicineIntro = medicineIntro
        db.session.add(model_medicine)
        db.session.commit()
        temp = {}
        temp["medicineName"] = medicineName
        temp["medicineIntro"] = medicineIntro
        data = []
        data.append(temp)
        return ops_renderJSON(msg="添加成功", data=data)
    return "添加成功"


@medicine.route("/update", methods=['POST'])
def updatemedicine():
    if request.method == 'POST':
        req = request.values
        medicineNameOld = req['medicineNameOld']
        medicineNameNew = req['medicineNameNew']
        medicineIntro = req['medicineIntro']
        medicineNameD = db.session.query(Medicine).filter_by(medicineName=medicineNameNew).first()
        if medicineNameD:
            return ops_renderErrJSON(msg="药品已经存在，请换一个再试试。")
        else:
            medicineNameU = db.session.query(Medicine).filter_by(medicineName=medicineNameOld).first()
            if medicineNameU != None:
                medicineNameU.medicineName = medicineNameNew
                medicineNameU.medicineIntro = medicineIntro
                db.session.commit()
                # json化data
                temp = {}
                temp["medicineName"] = medicineNameNew
                temp["medicineIntro"] = medicineIntro
                data = []
                data.append(temp)
                return ops_renderJSON(msg="修改成功", data=data)
            else:
                return ops_renderErrJSON(msg="不存在这个药品，无法修改")
    return "修改成功"


# 根据medicineName删除药品
@medicine.route("/delete", methods=['POST'])
def deletemedicine():
    from init import db
    if request.method == 'POST':
        res = request.values
        medicineName = res['medicineName']
        medicineNameD = db.session.query(Medicine).filter(Medicine.medicineName == medicineName).first()
        if medicineNameD == None:
            return ops_renderErrJSON(msg="目前没有该药品，请再次确认")
        medicineIntro = medicineNameD.medicineIntro

        temp = {}
        temp["medicineName"] = medicineName
        temp["medicineIntro"] = medicineIntro

        data = []
        data.append(temp)

        db.session.delete(medicineNameD)
        db.session.commit()

        return ops_renderJSON(msg="删除成功", data=data)


@medicine.route("/list", methods=['POST'])
def listMedicine():
    if request.method == 'POST':
        res = request.values
        page = int(res['page'])
        per_page = int(res['per_page'])
        if (page == None):
            page = 1
        if (per_page == None):
            per_page = 10
        result = Medicine.query.limit(per_page).offset((page - 1) * per_page)
        temp = {}
        data = []
        if (result != None):
            for i in result:
                temp["medicineName"] = i.medicineName
                temp["medicineIntro"] = i.medicineIntro
                data.append(temp.copy())
            return ops_renderJSON(msg="查询成功", data=data)
        else:
            return ops_renderErrJSON(msg="查询失败，目前没有药品")
