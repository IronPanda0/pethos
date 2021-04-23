from flask import Blueprint, request, make_response, render_template, jsonify
from flask_cors import CORS
from sqlalchemy import text
import json
from model.medicine import Medicine
from model.medicineroom import Medicineroom
from model.room import Room
from common.Response import ops_renderErrJSON, ops_renderJSON
from datetime import datetime, time

medicine = Blueprint('medicine', __name__, url_prefix='/medicine')


@medicine.route("/add", methods=['POST'])
def addmeMedicine():
    from init import db
    if request.method == "POST":
        req = request.values
        name = req['name']
        pay = req['pay']
        storage = req['storage']
        intro = req['intro']
        imgUrl = req['imgUrl']
        roomName = req['roomName']
        type = req['type']
        # 数据合法性检测
        nameD = Medicine.query.filter_by(name=name).first()
        if (nameD):
            return ops_renderErrJSON(msg="相同药品名已存在，请再换一个试试")
        roomNameD = Room.query.filter_by(roomName=roomName).first()
        if (roomNameD == None):
            return ops_renderErrJSON(msg="目前没有该科室，请再次检查")
        curRoomId = roomNameD.roomId
        # 写入数据库
        model_medicine = Medicine()
        model_medicine.name = name
        model_medicine.pay = pay
        model_medicine.storage = storage
        model_medicine.intro = intro
        model_medicine.imgUrl = imgUrl
        model_medicine.roomName = roomName
        model_medicine.type = type

        db.session.add(model_medicine)
        db.session.flush()
        model_medicineRoom = Medicineroom()
        model_medicineRoom.roomId = curRoomId
        model_medicineRoom.medicineId = model_medicine.medicineId
        db.session.add(model_medicineRoom)
        db.session.commit()

        temp = {}
        temp["name"] = name
        temp["intro"] = intro
        temp["pay"] = pay
        temp["storage"] = storage
        temp["imgUrl"] = imgUrl
        temp["roomName"] = roomName
        temp["type"] = type
        temp["medicineId"] = model_medicine.medicineId
        data = []
        data.append(temp)
        return ops_renderJSON(msg="药品添加成功", data=data)


@medicine.route("/update", methods=['POST'])
def updateMedicine():
    from init import db
    if request.method == 'POST':
        req = request.values
        medicineId = req['medicineId']
        nameNew = req['nameNew']
        roomName = req['roomName']
        storage = req['storage']
        pay = req['pay']
        intro = req['intro']
        imgUrl = req['imgUrl']
        type = req['type']
        nameD = db.session.query(Medicine).filter_by(name=nameNew).first()
        if nameD:
            return ops_renderErrJSON(msg="相同药品名已经存在，请换一个再试试。")
        else:
            medicineU = db.session.query(Medicine).filter_by(medicineId=medicineId).first()
            medicineRoomD = db.session.query(Medicineroom).filter_by(medicineId=medicineU.medicineId).first()
            curRoomD = db.session.query(Room).filter_by(roomName=roomName).first()
            if curRoomD == None:
                return ops_renderErrJSON(msg="目前没有该科室，请确认后再修改")
            else:
                curRoomId = curRoomD.roomId
                medicineRoomD.roomId = curRoomId
                medicineU.name = nameNew
                medicineU.storage = storage
                medicineU.pay = pay
                medicineU.intro = intro
                medicineU.imgUrl = imgUrl
                medicineU.roomName = roomName
                medicineU.type = type
                db.session.commit()

                # json化data
                temp = {}
                temp["name"] = nameNew
                temp["storage"] = storage
                temp['pay'] = pay
                temp["intro"] = intro
                temp["imgUrl"] = imgUrl
                temp["roomName"] = roomName
                temp["type"] = type
                temp["medicineId"] = medicineId
                data = []
                data.append(temp)
                return ops_renderJSON(msg="修改药品成功", data=data)


# 根据medicineName删除药品
@medicine.route("/delete", methods=['POST'])
def deleteMedicine():
    from init import db
    if request.method == 'POST':
        res = request.values
        medicineId = res['medicineId']
        medicineD = db.session.query(Medicine).filter_by(medicineId=medicineId).first()
        if medicineD == None:
            return ops_renderErrJSON(msg="目前没有该药品，请再次确认")
        else:
            name = medicineD.name
            intro = medicineD.intro
            storage = medicineD.storage
            imgUrl = medicineD.imgUrl
            roomName = medicineD.roomName
            pay = medicineD.pay
            type = medicineD.type
            temp = {}
            temp["name"] = name
            temp["intro"] = intro
            temp["pay"] = pay
            temp["storage"] = storage
            temp["imgUrl"] = imgUrl
            temp["roomName"] = roomName
            temp["type"] = type
            temp["medicineId"] = medicineId
            data = []
            data.append(temp)
            roomD = db.session.query(Room).filter_by(roomName=roomName).first()
            curRoomId = roomD.roomId
            medicineRoomD = db.session.query(Medicineroom).filter_by(medicineId=medicineId, roomId=curRoomId).first()
            db.session.delete(medicineRoomD)
            db.session.delete(medicineD)
            db.session.commit()

            return ops_renderJSON(msg="删除成功", data=data)


@medicine.route("/list", methods=['POST'])
def listmedicine():
    if request.method == 'POST':
        res = request.values
        page = res['page']
        per_page = res['per_page']
        roomName = res['roomName']
        type = res['type']
        if (page == ''):
            page = 1
        else:
            page = int(page)
        if (per_page == ''):
            per_page = 10
        else:
            per_page = int(per_page)
        if (len(roomName) == 0):
            result = Medicine.query.filter_by(type=type).limit(per_page).offset((page - 1) * per_page)
        else:
            result = Medicine.query.filter_by(roomName=roomName, type=type).limit(per_page).offset(
                (page - 1) * per_page)
        temp = {}
        data = []
        if (result.count() != 0):
            for i in result:
                temp["name"] = i.name
                temp["intro"] = i.intro
                temp["intro"] = i.intro
                temp['pay'] = i.pay
                temp["imgUrl"] = i.imgUrl
                temp["type"] = i.type
                temp["medicineId"] = i.medicineId
                data.append(temp.copy())
            return ops_renderJSON(msg="查询成功", data=data)
        else:
            return ops_renderErrJSON(msg="查询失败，目前没有药品")
